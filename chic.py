from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(image, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    response = model.generate_content([prompt, image[0]])
    return response.text

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

# Page configuration with custom styling
st.set_page_config(
    page_title="WebChic.ai",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with bolder styling and description
st.markdown("""
    <style>
    .main {
        padding: 1rem;
    }
    .big-title {
        font-size: 4rem !important;
        font-weight: 800 !important;
        background: linear-gradient(45deg, #FF4B4B, #FF8C8C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.5rem !important;
        font-weight: 500 !important;
        color: #666666;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .description {
        font-size: 1.1rem !important;
        color: #888888;
        text-align: center;
        max-width: 800px;
        margin: 0 auto 2rem auto;
        line-height: 1.6;
    }
    .features {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-bottom: 2rem;
        flex-wrap: wrap;
        text-align: center;
    }
    .feature-item {
        color: #666666;
        font-size: 1rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        padding: 0.75rem 1rem;
        border-radius: 5px;
        border: none;
        margin-top: 1rem;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .analysis-text {
        font-size: 1.1rem;
        line-height: 1.6;
        color: #333333;
    }
    .upload-text {
        font-size: 1.2rem;
        color: #666666;
        text-align: center;
        margin: 2rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header with description
st.markdown("<h1 class='big-title'>WebChic.ai</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>Your AI Fashion Advisor</h3>", unsafe_allow_html=True)
st.markdown("""
    <p class='description'>
        Upload any outfit photo and let our AI analyze it! Get personalized recommendations on when and where to wear it, 
        along with perfectly matching accessories. Perfect for planning your outfits or getting a second opinion on your style choices.
    </p>
    <div class='features'>
        <div class='feature-item'>✨ Seasonal Recommendations</div>
        <div class='feature-item'>🕒 Time-of-Day Suggestions</div>
        <div class='feature-item'>👗 Occasion Matching</div>
        <div class='feature-item'>💎 Accessory Advice</div>
    </div>
""", unsafe_allow_html=True)

# Create two columns for layout
col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader("Upload your outfit image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        # Calculate aspect ratio and set max height
        max_height = 500
        aspect_ratio = image.size[0] / image.size[1]
        width = int(max_height * aspect_ratio)
        image = image.resize((width, max_height))
        st.image(image, use_column_width=True)
    
    analyze_button = st.button("Analyze Outfit")

with col2:
    if uploaded_file is not None and analyze_button:
        with st.spinner("Analyzing your outfit..."):
            input_prompt = """
            Act as a fashion expert and analyze the outfit in the provided image. Provide a detailed breakdown of where and how this outfit can be worn, including:

            Best month(s) of the year to wear it (considering weather and seasonal trends).
            Time of day (daytime, nighttime, or both) it is most suitable for.
            Type of occasion (e.g., casual, formal, business, party, wedding, outdoor, etc.).
            Style category (e.g., casual, semi-formal, formal, streetwear, etc.).

            After this analysis, suggest matching accessories (e.g., jewelry, bags, shoes, belts, scarves, etc.) that would perfectly complement the outfit.
            """
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_response(image_data, input_prompt)
            
            st.markdown("<div class='analysis-text'>", unsafe_allow_html=True)
            st.write(response)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<p class='upload-text'>Upload an image and click 'Analyze Outfit' to get your fashion analysis</p>", unsafe_allow_html=True)
