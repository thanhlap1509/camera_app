import streamlit as st
from PIL import Image

with st.expander("Tách tách mfcker"):
    camera_image = st.camera_input("Chụp ảnh không em")


if camera_image:
        img = Image.open(camera_image)
        gray_scale = img.convert("L")
        st.image(gray_scale)