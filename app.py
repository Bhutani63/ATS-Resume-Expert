from dotenv import load_dotenv

load_dotenv()

import fitz  # PyMuPDF
import base64
import streamlit as st
import os
import io
from PIL import Image
# import pdf2image --As it was need the Poppler installation on my Windows machine,
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-2.0-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Read the PDF bytes from upload
        pdf_bytes = uploaded_file.read()

       # Open the PDF document from bytes
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")

        # Render the first page to an image
        first_page = pdf_document.load_page(0)  # page numbering starts from 0
        pix = first_page.get_pixmap()  # render page to image

        # Save image to bytes buffer in JPEG format
        img_byte_arr = pix.tobytes(output="jpeg")

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64 string
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file Uploaded")
    
## Streamlit App

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"]) 

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell me About the Resume")

# submit2 = st.button("How can I improvise my Skills")

submit3 = st.button("percentage match")

input_prompt1 = """
 You are an experienced HR with Tech Experience in the field of any one job role from Data Science, Full Stack Web development, Big Data Engineering,
  DEVOPS, Data Analyst, GenAI Engineering, ML Engineering, AI Engineering, Your task is to review the provided resume 
  against the Job description for these profiles. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role.
  Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
 You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of any one job role Data Science, Full Stack Web development, 
 Big Data Engineering, DEVOPS, Data Analyst, GenAI Engineering, ML Engineering, AI Engineering and deep functionality, 
  your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
  the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""
if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1, pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3, pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

