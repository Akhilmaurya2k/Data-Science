import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import google.generativeai as genai
import random
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

# Function to generate words using Gemini (LLM)
def generate_words(api_key):
    # Initialize Chat Model with the Google API Key and Model
    chat_model = ChatGoogleGenerativeAI(google_api_key=api_key, model="gemini-1.5-flash", temperature=1)

    # Define the prompt template
    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", """You are an AI words generator where you need to generate random creative words which can be drawn up to 5 only,
                          which are easy to draw, similar to Google Quick Draw words. Nothing else, only words and no numbering."""),
            ("human", "Generate a list of words based on the topic: {topic}")
        ]
    )

    # Define the output parser
    output_parser = CommaSeparatedListOutputParser()

    # Create the chain with prompt template, model, and output parser
    chain = chat_template | chat_model | output_parser

    # Provide user input for the topic
    user_input = {"topic": "creative and simple objects that can be drawn in 20 seconds"}

    # Invoke the chain with the user input
    result = chain.invoke(input=user_input)

    return result

# Main Streamlit app
st.set_page_config(page_title="Google QuickDraw Clone", page_icon="🎨")
st.title("QuickDraw Clone powered by Gemini")
st.markdown(
    """
    Welcome to QuickDraw!
    Unleash your inner artist and challenge our AI to guess your doodles. Draw, test, and see if our AI can keep up with your creativity. Let the fun begin!
    """
)

# Display the thinking GIF on the intro page
st.image("data/ai_thinking.gif", use_container_width=True)

# Load the API key
with open('keys/gemini_key.txt', 'r') as f:
    GOOGLE_API_KEY = f.read().strip()

# Configure the API key for the generative AI library
genai.configure(api_key=GOOGLE_API_KEY)

# Check if 'words' is already in session_state to avoid regenerating words
if "words" not in st.session_state:
    # Generate words only if they are not already in session_state
    words = generate_words(GOOGLE_API_KEY)
    st.session_state.words = words
    st.session_state.current_word_index = random.randint(0, len(words)-1)  # Select a random word index
    st.session_state.drawing_data = None  # Clear any previous drawing data

# Get the randomly selected word
selected_word = st.session_state.words[st.session_state.current_word_index]

# Display the word to draw (randomly selected)
st.subheader(f"Draw: {selected_word}")

# Canvas for drawing
col1, col2 = st.columns([0.7, 0.3])

with col1:
    drawing_mode = st.selectbox("Drawing tool:", ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"))
    stroke_width = st.slider("Stroke width: ", 1, 25, 3)
    if drawing_mode == "point":
        point_display_radius = st.slider("Point display radius: ", 1, 25, 3)
    stroke_color = st.color_picker("Stroke color hex: ")
    bg_color = st.color_picker("Background color hex: ", "#fff")

    canvas_result = st_canvas(
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        update_streamlit=True,
        width=480,
        drawing_mode=drawing_mode,
        point_display_radius=point_display_radius if drawing_mode == "point" else 0,
        key="canvas",
    )

with col2:
    st.write(f"Your word to draw: {selected_word}")

# If the user draws something, store the canvas result in session_state
if canvas_result.image_data is not None:
    st.session_state.drawing_data = canvas_result.image_data

# When the "Predict" button is clicked
if st.button("Predict") and st.session_state.drawing_data is not None:
    # Convert canvas drawing to JPEG format and send to LLM
    img = st.session_state.drawing_data
    img_pil = Image.fromarray(img)

    # If the image is in RGBA mode, convert it to RGB
    if img_pil.mode == 'RGBA':
        img_pil = img_pil.convert('RGB')

    # Save the image as a JPEG file on disk
    img_pil.save('output_image.jpeg', format='JPEG')

    # Optionally, reopen and display the image
    img = Image.open('output_image.jpeg')

    # Initialize the generative model
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    # Send image to LLM for prediction
    user_prompt = "The task as an AI bot is to predict the drawing from the canvas as a single word. Nothing else, only a single word."
    response = model.generate_content([img, user_prompt])

    # Get the predicted word
    predicted_word = response.text.strip()

    # Display the prediction
    st.write(f"Prediction: {predicted_word}")

    # Save both the selected word and the predicted word in a single string
    result_string = f"Actual word: {selected_word}, Predicted word: {predicted_word}"

    # Check if the predicted word matches the actual word
    if predicted_word.lower() == selected_word.lower():
        st.balloons()
        st.success("Great job! The prediction is correct!")
    else:
        st.subheader('Better luck next time')
        st.snow()
