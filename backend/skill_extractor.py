from skills import SKILLS

def extract_skills(text):

    detected_skills = []

    text = text.lower()

    for skill in SKILLS:

        if skill.lower() in text:
            detected_skills.append(skill)

    return detected_skills