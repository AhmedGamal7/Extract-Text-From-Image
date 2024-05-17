import streamlit as st
from PIL import Image
import pytesseract

def main():
    st.title("Image to Text Converter")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    language = st.selectbox("Language to convert", [
                            "English","Arabic"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        if st.button("Extract Text"):
            text = pytesseract.image_to_string(image,lang=language)
            st.header("Extracted Text")
            st.write(text)

if __name__ == "__main__":
    main()
