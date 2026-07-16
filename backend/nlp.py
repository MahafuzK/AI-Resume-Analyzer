import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_text(text):

    doc = nlp(text)

    return doc