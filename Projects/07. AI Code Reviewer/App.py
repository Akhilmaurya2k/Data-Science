import streamlit as st
from openai import OpenAI

# Setting up API key
with open('keys/openai_key.txt') as f:
    OPENAI_API_KEY = f.read().strip()

client = OpenAI(api_key=OPENAI_API_KEY)

st.title('AI Code Assistant')
st.caption('Powered by GenAI')

prompt = st.text_area(label='Enter your Python Code')
submit = st.button('Submit')

if submit:
    def python_compiler(prompt):
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using the "gpt-4o-mini" model
            messages=[
                {
                    "role": "system",
                    "content": """You are a Friendly Python Coding Assistant. When a user provides you with code, your role as the system is to:
                    
                    1. Give a Bug Report in normal text format with the heading 'Bug Report'. 
                    Review the code and provide optimized feedback on potential bugs along with suggestions for fixes.

                    2. Provide the fixed code without any comments, just clean code and with the heading 'Fixed Code' in a code block.
                      the code should be cleand nothing else apart from heading."""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        # Accessing the content correctly
        content = response.choices[0].message.content
        return content

    result = python_compiler(prompt)
    
    # Splitting the result into bug report and fixed code
    if "Fixed Code" in result:
        parts = result.split("Fixed Code")
        if len(parts) == 2:
            bug_report = parts[0].strip()
            fixed_code = parts[1].strip()
            fixed_code_1 = fixed_code.replace('```python', '').replace('```', '').strip()
            st.subheader('Bug Report')
            st.write(bug_report)
            st.subheader('Fixed Code')
            st.code(fixed_code_1)
        else:
            st.write("Unexpected result format. Please check the response.")
    else:
        st.write("Unexpected output format. Please check the response.")
