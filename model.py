import string
import fitz
import re
import json
import os

from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# -----------------------------------
# Load Semantic Model
# -----------------------------------

model = SentenceTransformer('paraphrase-MiniLM-L3-v2')

# -----------------------------------
# Skill List
# -----------------------------------

skills_file_path = os.path.join(os.path.dirname(__file__), 'data', 'skills.json')
try:
    with open(skills_file_path, 'r', encoding='utf-8') as f:
        skills_list = json.load(f)
except Exception as e:
    print(f"Error loading skills dataset: {e}")
    # Fallback minimal list just in case
    skills_list = ["python", "java", "sql", "react", "javascript"]

# -----------------------------------
# Pre-compile Skill Patterns
# -----------------------------------
# Using negative lookbehinds/lookaheads instead of \b to handle special characters (e.g. C++, .NET)
skill_patterns = {
    skill: re.compile(rf"(?<!\w){re.escape(skill.lower())}(?!\w)")
    for skill in skills_list
}

# -----------------------------------
# Text Preprocessing
# -----------------------------------

def preprocess(text):

    text = text.lower()

    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    return text


# -----------------------------------
# Fit Classification
# -----------------------------------

def get_fit(score):

    if score >= 70:
        return "Good"

    elif score >= 40:
        return "Average"

    else:
        return "Poor"


# -----------------------------------
# Extract Text From PDF
# -----------------------------------

def extract_text_from_pdf(pdf_file):

    text = ""

    try:
        pdf = fitz.open(
            stream=pdf_file.read(),
            filetype="pdf"
        )

        for page in pdf:

            text += page.get_text()
            
    except Exception as e:
        print(f"Error reading PDF: {e}")
        pass

    return text


# -----------------------------------
# Main Analysis Function
# -----------------------------------

def analyze_uploaded_resumes(job_descs, uploaded_files):

    # 1. Process all resumes first (extract text, encode once)
    resumes_data = []
    for file in uploaded_files:
        resume_text = extract_text_from_pdf(file)
        clean_resume = preprocess(resume_text)
        resume_embedding = model.encode(clean_resume)
        resumes_data.append({
            "name": file.filename,
            "text": resume_text,
            "clean_text": clean_resume,
            "embedding": resume_embedding
        })

    # 2. Compare against each Job Description
    all_results = []
    
    for jd in job_descs:
        jd_title = jd["title"]
        jd_text = jd["text"]
        
        clean_jd = preprocess(jd_text)
        jd_embedding = model.encode(clean_jd)
        jd_text_lower = jd_text.lower()
        
        jd_results = []
        for r_data in resumes_data:
            
            # Semantic Similarity Score
            score = cosine_similarity(
                [jd_embedding],
                [r_data["embedding"]]
            )[0][0] * 100
            
            resume_text_lower = r_data["text"].lower()
            
            # Matched Skills
            matched_skills = [
                skill for skill, pattern in skill_patterns.items()
                if pattern.search(resume_text_lower)
            ]
            
            # Missing Skills
            missing_skills = [
                skill for skill, pattern in skill_patterns.items()
                if pattern.search(jd_text_lower)
                and not pattern.search(resume_text_lower)
            ]
            
            jd_results.append({
                "name": r_data["name"],
                "score": round(score, 2),
                "fit": get_fit(score),
                "matched_skills": matched_skills,
                "missing_skills": missing_skills,
                "text": r_data["text"]
            })
            
        # Sort and Rank for this JD
        jd_results = sorted(jd_results, key=lambda x: x['score'], reverse=True)
        for i, r in enumerate(jd_results, start=1):
            r["rank"] = i
            
        all_results.append({
            "jd_title": jd_title,
            "candidates": jd_results
        })

    return all_results