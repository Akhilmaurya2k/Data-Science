# QuickDraw Clone Powered by Google Gemini LLM

## Overview
QuickDraw Clone is an interactive web application built using **Streamlit** that allows users to draw objects based on randomly generated words. The application uses **Google Gemini 1.5 LLM** for generating simple, drawable words and **Generative AI** to predict the objects drawn by users.

## Key Features
- **Word Generation**: The app uses **Google Gemini 1.5 LLM** to generate creative, simple words that are easy to draw.
- **Drawing Interface**: Users can draw the selected word using a variety of drawing tools on an interactive canvas.
- **Prediction System**: The **Google Gemini 1.5 LLM** analyzes the drawn image and provides a prediction of the object.
- **Visual Feedback**: Celebratory balloons appear when the prediction is correct, and snowflakes when it is incorrect.

## Technologies Used
- **Python**
- **Streamlit**
- **Google Gemini 1.5 LLM**
- **LangChain**
- **Streamlit Drawable Canvas**
- **Pillow (PIL)**

## Usage
1. Open the app in your browser.
2. A random word will be displayed for you to draw on the canvas.
3. Use the available drawing tools to sketch the word.
4. Click on **"Predict"** to allow the model to predict the object based on your drawing.
5. If the model correctly identifies the object, balloons will appear. If it’s incorrect, snowflakes will be shown.

## Jupyter Notebook
For additional exploration and experimentation, you can also review and run the **`quickdraw_notebook.ipynb`**. This notebook provides insights into the workings of the LLM and the data used in the app.

## Contributors
- **Akhil Padma**
