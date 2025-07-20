# keyword_tools.py

import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, max_keywords=8):
    if not text:
        return ["No keywords found."]
    
    doc = nlp(text)
    candidates = [token.lemma_.lower() for token in doc if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop]
    top = Counter(candidates).most_common(max_keywords)
    return [word for word, _ in top]