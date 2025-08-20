# orbit_snap.py

# Import python libraries for API key that will fetch NASA's Astronomy Picture of the Day
import requests
import streamlit as st
import spacy
import os
from collections import Counter
import warnings
from transformers import pipeline

# Layout Setup
st.set_page_config(page_title="Orbit Snap", layout="wide")

# NASA APOD API Setup
API_KEY = st.secrets["API_KEY"]
APOD_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

# Load summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# API Fetching
def fetch_apod_data():
    try:
        response = requests.get(APOD_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"NASA API error: {e}")
        return None

def display_apod(data):
    st.title("Astronomy Picture of the Day")
    
    if "url" in data:
        st.image(data['url'], caption=data.get('title', ''))

    st.subheader("Date")
    st.text(data.get('date', 'Unknown'))

    st.subheader("Description")
    st.write(data.get('explanation', 'No description available'))

    st.markdown(f"[View on NASA]({data.get('hdurl', '')})")

def main():
    st.sidebar.header("Orbit Snap Controls")
    st.sidebar.write("Fetching today’s space image.")
    
    apod_data = fetch_apod_data()
    
    # Import and Display keywords
    if apod_data:
        display_apod(apod_data)
        
        # spaCy Keyword Extractor
        nlp = spacy.load("en_core_web_sm")
        
        # Create a function to extract keywords using common NLP tools
        def extract_keywords(text, max_keywords=8):
            if not text:
                return ["No keywords found."]
            doc = nlp(text)
            candidates = [token.lemma_.lower() for token in doc if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop]
            top = Counter(candidates).most_common(max_keywords)
            return [word for word, _ in top]
        
        keywords = extract_keywords(apod_data.get('explanation', ''))
        st.subheader("Extracted Keywords")
        st.write(", ".join(keywords))
    
if __name__ == "__main__":
    main()

