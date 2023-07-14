import streamlit as st
from PIL import Image

with st.expander("Tách tách mfcker"):
    #mở cửa sổ chụp anh bằng method camera input
    camera_image = st.camera_input("Chụp ảnh không em")


if camera_image:
        # tạo instance của class Image
        img = Image.open(camera_image)
        #convert gray scale
        gray_scale = img.convert("L")
        #render ảnh gray scale ra màn hình
        st.image(gray_scale)