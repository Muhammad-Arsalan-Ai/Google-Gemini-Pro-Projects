# import streamlit as st
# import google.generativeai as genai
# import os
# import PyPDF2 as pdf
# from dotenv import load_dotenv
# import json


# load_dotenv() ## load all our environment variables

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_repsonse(input):
#     model=genai.GenerativeModel('gemini-pro')
#     response=model.generate_content(input)
#     return response.text

# def input_pdf_text(uploaded_file):
#     reader=pdf.PdfReader(uploaded_file)
#     text=""
#     for page in range(len(reader.pages)):
#         page=reader.pages[page]
#         text+=str(page.extract_text())
#     return text

# # Function to generate eligibility report
# def generate_eligibility_report(match_percentage, missing_skills, qualifications_summary):
#     eligibility_report = {
#         "JD Match": f"{match_percentage}%",
#         "MissingSkills": missing_skills,
#         "QualificationsSummary": qualifications_summary
#     }
#     return json.dumps(eligibility_report)
# #Prompt Template

# input_prompt="""
# Hey Act Like a skilled or very experience ATS(Application Tracking System)
# with a deep understanding of tech field,software engineering,data science ,data analyst
# and big data engineer. Your task is to evaluate the resume based on the given job description.
# You must consider the job market is very competitive and you should provide 
# best assistance for improving thr resumes. Assign the percentage Matching based 
# on Jd and
# the missing keywords with high accuracy
# resume:{text}
# description:{jd}

# I want the response in one single string having the structure
# {{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
# """

# ## streamlit app
# st.title("Smart ATS")
# st.text("Improve Your Resume ATS")
# jd=st.text_area("Paste the Job Description")
# uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

# submit = st.button("Submit")

# if submit:
#     if uploaded_file is not None:
#         text=input_pdf_text(uploaded_file)
#         response=get_gemini_repsonse(input_prompt)
#         st.subheader(response)


# import streamlit as st
# import google.generativeai as genai
# import os
# import PyPDF2 as pdf
# from dotenv import load_dotenv
# import json


# load_dotenv() ## load all our environment variables

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input):
#     model=genai.GenerativeModel('gemini-pro')
#     response=model.generate_content(input)
#     return response.text

# def input_pdf_text(uploaded_file):
#     reader=pdf.PdfReader(uploaded_file)
#     text=""
#     for page in range(len(reader.pages)):
#         page=reader.pages[page]
#         text+=str(page.extract_text())
#     return text

# # Function to generate eligibility report
# def generate_eligibility_report(match_percentage, missing_skills, qualifications_summary):
#     eligibility_report = {
#         "JD Match": f"{match_percentage}%",
#         "MissingSkills": missing_skills,
#         "QualificationsSummary": qualifications_summary
#     }
#     return json.dumps(eligibility_report)
# #Prompt Template

# input_prompt="""
# Hey Act Like a skilled or very experience ATS(Application Tracking System)
# with a deep understanding of tech field,software engineering,data science ,data analyst
# and big data engineer. Your task is to evaluate the resume based on the given job description.
# You must consider the job market is very competitive and you should provide 
# best assistance for improving thr resumes. Assign the percentage Matching based 
# on Jd and
# the missing keywords with high accuracy
# resume:{text}
# description:{jd}

# I want the response in one single string having the structure
# {{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
# """

# ## streamlit app
# st.title("Smart ATS")
# st.text("Improve Your Resume ATS")
# jd=st.text_area("Paste the Job Description")
# uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

# submit = st.button("Submit")

# if submit:
#     if uploaded_file is not None:
#         text = input_pdf_text(uploaded_file)
#         response = get_gemini_response(input_prompt.format(text=text, jd=jd))
#         response_dict = json.loads(response)

#         st.markdown("## ATS Evaluation Result")
#         st.write(f"JD Match: **{response_dict['JD Match']}**")
        
#         st.markdown("## Missing Skills:")
#         for skill in response_dict['MissingKeywords']:
#             st.write(f"- {skill}")
        
#         st.markdown("## Qualifications Summary:")
#         st.write(response_dict['Profile Summary'])


import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import random
import string
import numpy as np


load_dotenv()  ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# def get_gemini_response(input, temperature=0.0):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content(input, temperature=temperature)
#     return response.text

import multiprocessing

# Function to generate Gemini response in a separate process
def generate_gemini_response(input, output_queue):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    response_text = response.text
    output_queue.put(response_text)

def get_gemini_response(input):
    output_queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=generate_gemini_response, args=(input, output_queue))
    process.start()
    process.join()

    response_text = output_queue.get()
    return response_text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


# Function to generate eligibility report
def generate_eligibility_report(match_percentage, missing_skills, qualifications_summary):
    eligibility_report = {
        "JD Match": f"{match_percentage}%",
        "MissingSkills": missing_skills,
        "QualificationsSummary": qualifications_summary
    }
    return json.dumps(eligibility_report)


# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

## Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt.format(text=text, jd=jd))
        response_dict = json.loads(response)

        st.markdown("## ATS Evaluation Result")
        st.write(f"JD Match: **{response_dict['JD Match']}**")

        st.markdown("## Missing Skills:")
        for skill in response_dict['MissingKeywords']:
            st.write(f"- {skill}")

        st.markdown("## Qualifications Summary:")
        st.write(response_dict['Profile Summary'])


