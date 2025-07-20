# keyword_tools.py
# spaCy Keyword Extractor
# !pip install spacy - uncomment this line of code if you don't have spacy installed
import spacy
import subprocess
from collections import Counter

# Download model if not present
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")

# Create a function to extract keywords using common NLP tools
def extract_keywords(text, max_keywords=8):
    if not text:
        return ["No keywords found."]
    
    doc = nlp(text)
    candidates = [token.lemma_.lower() for token in doc if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop]
    top = Counter(candidates).most_common(max_keywords)
    return [word for word, _ in top]
