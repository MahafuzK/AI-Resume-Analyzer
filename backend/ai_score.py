from skill_extractor import extract_skills
from embeddings import semantic_score


def calculate_ai_scores(
    resume_sections,
    jd_sections
):

    scores = {}

    # -----------------------------
    # Skills Score
    # -----------------------------

    resume_skills = extract_skills(
        resume_sections["skills"]
    )

    jd_skills = extract_skills(
        jd_sections["skills"]
    )

    if len(jd_skills) > 0:

        matched = len(
            set(resume_skills) &
            set(jd_skills)
        )

        skills_score = (
            matched /
            len(jd_skills)
        ) * 100

    else:

        skills_score = 0

    scores["skills"] = round(skills_score, 2)

    # -----------------------------
    # Projects Score
    # -----------------------------

    scores["projects"] = semantic_score(

        resume_sections["projects"],

        jd_sections["responsibilities"]

    )

    # -----------------------------
    # Education Score
    # -----------------------------

    scores["education"] = semantic_score(

        resume_sections["education"],

        jd_sections["qualification"]

    )

    # -----------------------------
    # Experience
    # -----------------------------

    scores["experience"] = 0

    return scores