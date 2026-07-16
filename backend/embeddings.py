from sentence_transformers import SentenceTransformer
from sentence_transformers import util

model = SentenceTransformer("all-MiniLM-L6-v2")
def calculate_similarity(text1, text2):

    embedding1 = model.encode(text1, convert_to_tensor=True)

    embedding2 = model.encode(text2, convert_to_tensor=True)

    similarity = util.cos_sim(embedding1, embedding2)

    return similarity.item()

def get_embedding(text):

    return model.encode(text, convert_to_tensor=True)

def semantic_score(resume_text, jd_text):

    resume_embedding = get_embedding(resume_text)

    jd_embedding = get_embedding(jd_text)

    similarity = util.cos_sim(resume_embedding, jd_embedding)

    return round(similarity.item() * 100, 2)

def section_semantic_scores(sections, jd_text):

    scores = {}

    for section, content in sections.items():

        if content.strip():

            scores[section] = semantic_score(content, jd_text)

        else:

            scores[section] = 0

    return scores

# def compare_resume_jd_sections(resume_sections, jd_sections):

#     scores = {}

#     scores["skills"] = semantic_score(
#         resume_sections["skills"],
#         jd_sections["skills"]
#     )

#     scores["projects"] = semantic_score(
#         resume_sections["projects"],
#         jd_sections["responsibilities"]
#     )

#     scores["education"] = semantic_score(
#         resume_sections["education"],
#         jd_sections["qualification"]
#     )

#     scores["experience"] = 0

#     return scores