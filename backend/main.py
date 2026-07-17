from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from parser import extract_text_from_pdf
from skill_extractor import extract_skills
from ats import calculate_ats_score
from suggestions import generate_suggestions
from nlp import analyze_text
# from embeddings import compare_resume_jd_sections
from feedback import generate_feedback
from resume_sections import extract_sections
from jd_parser import extract_jd_sections
from ai_score import calculate_ai_scores
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Analyzer 🚀"
    }


@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    # Save uploaded resume
    file_path = os.path.join("uploads", resume.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    # Extract Resume Text
    text = extract_text_from_pdf(file_path)

    # -----------------------------
    # Resume Sections
    # -----------------------------
    sections = extract_sections(text)
    jd_sections = extract_jd_sections(job_description)

    print("\n========== JD Sections ==========")

    for section, content in jd_sections.items():

        print(f"\n----- {section.upper()} -----")

        print(content[:500])

    print("\n========== Resume Sections ==========")

    for section, content in sections.items():

        print(f"\n----- {section.upper()} -----")

        print(content[:500])

    # -----------------------------
    # Section Semantic Scores
    # -----------------------------
    section_scores = calculate_ai_scores(
    sections,
    jd_sections
)

    print("\n========== Section Semantic Scores ==========")

    for section, score in section_scores.items():

        print(f"{section}: {score}")
    
    # ----------------------------------
    # Adaptive Weighted AI Semantic Score
    # ----------------------------------

    weights = {
        "skills": 0.40,
        "projects": 0.30,
        "experience": 0.20,
        "education": 0.10
    }

    # Keep only sections that actually exist
    available_sections = {}

    for section, score in section_scores.items():

        if score > 0:
            available_sections[section] = score

    # Total weight of available sections
    total_weight = 0

    for section in available_sections:
        total_weight += weights[section]

    # Calculate normalized weighted score
    ai_score = 0

    for section, score in available_sections.items():

        normalized_weight = weights[section] / total_weight

        ai_score += score * normalized_weight

    ai_score = round(ai_score, 2)

    print("\n========== Adaptive Weighted AI Score ==========")
    print(ai_score)

    # -----------------------------
    # spaCy Analysis
    # -----------------------------
    doc = analyze_text(text)

    print("\n========== Named Entities ==========")

    for ent in doc.ents:
        print(f"{ent.text} --> {ent.label_}")

    # -----------------------------
    # Skill Extraction
    # -----------------------------
    resume_skills = extract_skills(text)
    jd_skills = extract_skills(job_description)

    # -----------------------------
    # ATS Score
    # -----------------------------
    result = calculate_ats_score(
        resume_skills,
        jd_skills
    )

    # -----------------------------
    # Suggestions
    # -----------------------------
    suggestions = generate_suggestions(
        result["missing_skills"]
    )

    # -----------------------------
    # Feedback
    # -----------------------------
    feedback = generate_feedback(
        result["score"],
        ai_score,
        result["missing_skills"]
    )

    print("\n========== Resume Skills ==========")
    print(resume_skills)

    print("\n========== JD Skills ==========")
    print(jd_skills)

    print("\n========== ATS Result ==========")
    print(result)

    # -----------------------------
    # API Response
    # -----------------------------
    return {

        "filename": resume.filename,

        "ats_score": result["score"],

        "semantic_score": ai_score,

        # "section_scores": section_scores,

        "resume_skills": resume_skills,

        "jd_skills": jd_skills,

        "matched_skills": result["matched_skills"],

        "missing_skills": result["missing_skills"],

        "suggestions": suggestions,

        "feedback": feedback,

        "section_scores": section_scores

    }