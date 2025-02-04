### Health Management APP
from dotenv import load_dotenv

load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import pandas as pd

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([image[0],prompt])  # Ensure correct order
    return response.text if hasattr(response, 'text') else str(response)

def get_gemini_response2(text, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([text,prompt])  # Ensure correct order
    return response.text if hasattr(response, 'text') else str(response)

def get_gemini_response3(text,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([text,prompt])  # Ensure correct order
    return response.text if hasattr(response, 'text') else str(response)



def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Initialize our Streamlit app
st.set_page_config(page_title="Gemini Health App")

st.header("Gemini Health App")
user_input = st.text_input("Input Prompt: ", key="input")  # Renamed input to user_input
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = None  # Initialize image variable
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
elif user_input:
    # If user input is provided, use it as the prompt
    prompt = user_input
    response = get_gemini_response2(user_input, prompt)

submit = st.button("Tell me the total calories")

input_prompt = """
do not type this "It's impossible to give exact calorie counts for this bowl without knowing the precise quantities of each ingredient."
You are an expert nutritionist. Analyze the food items from the image 
and calculate the total calories. if the range is from A-B... tell the calories ranges from A - B and No warnings,No need to advice about the exact calories. Also, provide details of each food item with its calorie intake 
in the following format: 

1. Item 1 - no of calories
2. Item 2 - no of calories
----
----
"""

input_prompt2 = """
You are an expert nutritionist. Tell Calories for one serving. Tell me the name of the dish as well at the start.
Dont tell Anything about Ingredients of the dish or Instructions on how to make it.
the format should be like:

For one serving the macro nutrients are :
Protein : 
Carbs : 
Fiber :
-----
-----

dont need to give a note or disclaimer or warning.


"""

store_name = " You are an expert nutritionist. Give me the name of the dish from the text and its Calories and no extra details about it.The format must always be like 'dish_name':'interger_value', dish_name is the name of the dish in text ive given. if the calories ranges from A to B...give me the Bs value.No extra warnings or advices.dont need to give me It's impossible to determine the caloric value of a dish based solely on its macronutrient ranges.  More information is needed, such as the specific types of carbohydrates and fats present."

## If submit button is clicked
if submit:
    if uploaded_file:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(image_data, input_prompt)
        x = get_gemini_response3(response,store_name)
        st.subheader("The Response is")
        st.write(response)
        print(x)
    
    elif user_input:
        # If user input is provided, use it as the prompt
        prompt = user_input
        response = get_gemini_response2(user_input, input_prompt2)
        x = get_gemini_response3(response,store_name)
        st.subheader("The Response is")
        st.write(response)
        print(x)
    else:
        st.error("Please upload an image before submitting.")