import streamlit as st
from resume_parser import extract_resume_text
from text_processing import preprocess
from matcher import calculate_match, missing_skills

st.title("AI Resume Analyzer")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if resume_file and job_desc:
    with open("temp_resume.pdf", "wb") as f:
        f.write(resume_file.read())

    resume_text = preprocess(extract_resume_text("temp_resume.pdf"))
    job_text = preprocess(job_desc)

    score = calculate_match(resume_text, job_text)
    gaps = missing_skills(resume_text, job_text)

    st.subheader(f"Match Score: {score}%")
    st.write("Missing Skills (Top 10):", gaps[:10])
