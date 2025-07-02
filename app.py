import streamlit as st
import google.generativeai as genai
from PIL import Image

# Set your Gemini API key
genai.configure(api_key="AIzaSyAc6ctooYBucHy1dvONh6IPPRqBX4U4H68")

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI
st.title("🛍️ Automated Product Description Writer with Image Support")
st.write("Upload a product image and provide details to generate a catchy, SEO-friendly description.")

# Image upload
uploaded_image = st.file_uploader("Upload Product Image (optional)", type=["jpg", "jpeg", "png"])

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Product Image", use_column_width=True)

# Text inputs
product_name = st.text_input("Product Name", placeholder="e.g., UltraComfort Office Chair")
features = st.text_area("Key Features", placeholder="e.g., Ergonomic design, Adjustable height, Breathable mesh back")
audience = st.text_input("Target Audience", placeholder="e.g., Office workers, Gamers")

tone = st.selectbox("Choose Tone", ["Professional", "Friendly", "Luxury", "Casual"])

if st.button("Generate Description"):
    if not product_name or not features or not audience:
        st.warning("Please fill in all the fields!")
    else:
        # Prepare image reference text (optional)
        image_context = "The user has also provided a product image. Consider that while generating the description." if uploaded_image else ""

        # Create prompt
        prompt = f"""
Write a {tone.lower()} and SEO-friendly product description for the following:

Product Name: {product_name}
Key Features: {features}
Target Audience: {audience}

{image_context}

The description should be persuasive, highlight the features, and appeal to the audience.
"""

        # Generate description
        response = model.generate_content(prompt)
        description = response.text

        st.subheader("✨ Generated Product Description")
        st.write(description)

        st.download_button("Download Description", description, file_name="product_description.txt", mime="text/plain")
