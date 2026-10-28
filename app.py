import requests
import streamlit as st

filepath = 'news.img'
api = ""
url = ("https://science.nasa.gov/wp-json/wp/v2/apod-basic?"
       f"api_key={api}")

request = requests.get(url)
content = request.json()

request2 = requests.get(content[0]['hdurl'])
img = request2.content

with open(filepath, 'wb') as f:
    f.write(img)

st.title(content[0]["title"])
st.image(filepath)
st.markdown(content[0]['explanation'], unsafe_allow_html=True)