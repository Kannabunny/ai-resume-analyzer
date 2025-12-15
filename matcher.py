from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume_text, job_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_text])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return round(similarity[0][0] * 100, 2)

def missing_skills(resume_text, job_text):
    resume_set = set(resume_text.split())
    job_set = set(job_text.split())
    return list(job_set - resume_set)
