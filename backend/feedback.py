def generate_feedback(ats_score, semantic_score, missing_skills):

    strengths = []
    weaknesses = []
    recommendations = []

    # ATS Score
    if ats_score >= 80:
        strengths.append("Excellent keyword match with the job description.")
    elif ats_score >= 60:
        strengths.append("Good keyword coverage.")
    else:
        weaknesses.append("Low keyword match with the job description.")

    # Semantic Score
    if semantic_score >= 70:
        strengths.append("Resume content aligns well with the job description.")
    elif semantic_score >= 40:
        weaknesses.append("Resume is only partially aligned with the job description.")
    else:
        weaknesses.append("Resume content has low semantic relevance to the job description.")

    # Missing Skills
    if missing_skills:
        recommendations.append(
            "Add these important skills: " +
            ", ".join(missing_skills)
        )

    # General Advice
    recommendations.append(
        "Quantify project achievements using numbers wherever possible."
    )

    recommendations.append(
        "Keep your resume concise and ATS-friendly."
    )

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendations": recommendations
    }