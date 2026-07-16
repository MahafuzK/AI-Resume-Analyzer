def calculate_ats_score(resume_skills, jd_skills):

    resume_skill_set = set(resume_skills)

    matched_skills = []
    missing_skills = []

    for skill in jd_skills:

        if skill in resume_skill_set:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    score = 0

    if len(jd_skills) > 0:
        score = (len(matched_skills) / len(jd_skills)) * 100

    return {
        "score": round(score),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }