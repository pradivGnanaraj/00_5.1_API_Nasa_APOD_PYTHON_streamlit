import requests
import streamlit as st
from PIL import Image
import io

def download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful (status code 200)

        with open(save_path, 'wb') as f:
            f.write(response.content)
        
        print(f"Image downloaded and saved to '{save_path}'.")
        return save_path

    except requests.exceptions.RequestException as e:
        print(f"Error while downloading the image: {e}")
        return None

# Your code continues...
api_key = "XWcAPCXvGEXEdo1Dyggv22lkhFZBp7F5d4HFrSq7"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
request = requests.get(url)
content = request.json()

# Get the image 
img_url = content["url"]
img_path = "todays_image.jpg"

downloaded_image_path = download_image(img_url, img_path)

if downloaded_image_path:
    image = Image.open(downloaded_image_path)

st.set_page_config(layout="wide")

# st.write["Astronomy Picture of the Day"]

col1, col2 = st.columns(2)

with col1:
    st.write(content["date"])
    st.write(content["title"])
    if downloaded_image_path:
        st.image(image, caption=content["title"])

with col2:
    st.write(content["explanation"])
