import streamlit as st
from PIL import Image
import pytesseract

def main():
    st.title("Image to Text Converter")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        text = pytesseract.image_to_string(image)
        st.header("Extracted Text")
        st.write(text)

if __name__ == "__main__":
    main()
