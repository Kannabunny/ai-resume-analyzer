\# AI Resume Analyzer



An AI-powered web application that analyzes resumes against job descriptions using Natural Language Processing (NLP) and provides a match score along with missing skills.



\## 🚀 Features

\- Upload resume in PDF format

\- Paste job description text

\- Resume and job description matching using NLP

\- Match score calculation using cosine similarity

\- Identification of missing skills

\- Interactive web interface using Streamlit



\## 🛠 Tech Stack

\- Python

\- spaCy

\- scikit-learn

\- pdfminer.six

\- Streamlit

\- NLP



\## ⚙️ How It Works

1\. Extracts text from resume PDF

2\. Preprocesses text using NLP techniques

3\. Converts text to TF-IDF vectors

4\. Computes similarity using cosine similarity

5\. Displays match score and missing skills



\## 📦 Installation

```bash

git clone https://github.com/Kannabunny/ai-resume-analyzer.git

cd ai-resume-analyzer

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

python -m spacy download en\_core\_web\_sm



