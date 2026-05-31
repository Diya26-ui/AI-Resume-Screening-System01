import streamlit as st
import pdfplumber

st.title("AI Resume Screening System")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume uploaded successfully!")

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    st.subheader("Resume Preview")

    st.text(text[:2000])