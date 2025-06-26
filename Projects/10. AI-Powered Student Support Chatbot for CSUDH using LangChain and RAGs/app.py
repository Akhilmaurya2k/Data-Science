import streamlit as st

# Setup OpenAI Key
with open("keys/openai_key.txt", "r") as f:
    OPENAI_API_KEY = f.read().strip()

# 1. Load LangChain components for RAG
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 2. Setup Embedding model
embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# 3. Connect to ChromaDB (or create if not exists)
db = Chroma(
    collection_name="vector_database",
    embedding_function=embedding_model,
    persist_directory="./chroma_db_"
)
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 10})

# 4. Define the RAG prompt
PROMPT_TEMPLATE = """
Answer the question based only on the following context for the MS in Computer Science 
program at CSUDH: {context} 

Answer the question based on the above context: {question}. 
Provide a detailed answer. 
Do not provide any information beyond what is included in the context.
"""
prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

# 5. Setup Chat Model
chat_model = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini", temperature=1)
parser = StrOutputParser()

# 6. Format retrieved docs
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 7. RAG chain
rag_chain = {
    "context": retriever | format_docs,
    "question": RunnablePassthrough()
} | prompt_template | chat_model | parser


# 8. Streamlit UI Setup
st.title("🎓 CSUDH Chatbot")

# Assistant's greeting
st.chat_message("assistant").write("Hello! How can I assist you today? If you have any questions or need help with Ask Teddy, feel free to ask anything.  ")

# Session state to maintain conversation
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Show previous messages
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Ask a question about CSUDH MS in CS")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Get RAG response
    with st.spinner("Thinking..."):
        try:
            response = rag_chain.invoke(user_input)
        except Exception as e:
            response = "Sorry, I couldn't process your question at the moment. Please try again later."
            print(e)

    # Append and display assistant response
    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
