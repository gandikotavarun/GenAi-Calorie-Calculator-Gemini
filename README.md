# GenAi-Calorie-Calculator-Gemini
## Overview  
The **Calorie-Calculator App** is a Streamlit-based web application that leverages **Google Gemini Vision API** to analyze food images and text inputs to estimate calorie content. The app is designed to assist users in understanding the nutritional value of their meals in a simple and interactive way.  

## Features  
- **Image-Based Calorie Estimation:** Upload an image of food, and the app will analyze it to estimate the total calories and provide a breakdown of individual food items.  
- **Text-Based Nutrition Analysis:** Enter a text description of a dish to receive an estimated calorie count and macronutrient details.  
- **Google Gemini AI Integration:** Uses **Google Gemini Vision API** for advanced image and text processing.  
- **User-Friendly Interface:** Built with **Streamlit** for an intuitive and responsive UI.  

## How It Works  
1. **Upload an image** of your meal or enter a text description.  
2. The app processes the input using **Google Gemini AI** and returns a calorie estimate.  
3. The results include a **breakdown of individual food items** along with their calorie values.  
4. If using text input, the app also provides **macronutrient details** (Protein, Carbs, Fiber, etc.).  

## Technologies Used  
- **Python**  
- **Streamlit** (for UI)  
- **Google Gemini API** (for AI-driven food recognition)  
- **Pandas** (for data processing)  
- **PIL (Pillow)** (for image handling)  
- **dotenv** (for managing API keys securely)  

## Usage  
- **Upload an Image:** Click "Choose an image..." and upload a food image.  
- **Text Input:** Enter a dish name or description.  
- Click **"Tell me the total calories"** to generate a response.  

## Future Enhancements  
- **Improve Food Recognition Accuracy**  
- **Expand Nutritional Insights** (Micronutrient details, dietary recommendations)  
- **Support for Multiple API Providers**  


