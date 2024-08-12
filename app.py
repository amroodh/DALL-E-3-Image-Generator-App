from openai import OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey

client = OpenAI(api_key=apikey)


def generate_images(image_description, num_images):
    response = client.images.generate(
        model="dall-e-3",
        prompt=image_description,
        size="1024x1024",
        quality="standard",
        n=1
    )
    image_url = response.data[0].url
    return image_url


st.set_page_config(page_title="Dall-E-Image-Generator", page_icon=":camera:", layout="wide")

st.title("Dall-E-3 Image Generation Tool")

st.subheader("POWERED BY the World's Most POWERFUL Image Generation API- DALL-E")
img_description = st.text_input("Enter the description for the image you want ot generate")
num_of_images = st.number_input("Select the number of images you want to generate", min_value=1, max_value=10, value=1)

if st.button("Generate Images"):
    generate_image = generate_images(img_description, num_of_images)
    st.image(generate_image)
