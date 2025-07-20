# orbit_snap.py

# Import python libraries for API key that will fetch NASA's Astronomy Picture of the Day
#!pip install streamlit transformers requests
import requests
import streamlit as st
from transformers import pipeline
from keyword_tools import extract_keywords

# NASA APOD API Setup
API_KEY = "zSKrKQgBxbgjf7aMxT2Z3T9a5RVrCnRsZdJS6lCQ"
APOD_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

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
    st.title(" Astronomy Picture of the Day")
    
    if "url" in data:
        st.image(data['url'], caption=data.get('title', ''), use_column_width=True)

    st.subheader("Date")
    st.text(data.get('date', 'Unknown'))

    st.subheader("Description")
    st.write(data.get('explanation', 'No description available'))

    st.markdown(f"[View on NASA]({data.get('hdurl', '')})")

def main():
    st.sidebar.header("🚀 Orbit Snap Controls")
    st.sidebar.write("Fetching today’s space image...")

    apod_data = fetch_apod_data()
    if apod_data:
        display_apod(apod_data)

if __name__ == "__main__":
    main()

# Import and Display keywords
data = fetch_apod_data()
if data:
    keywords = extract_keywords(data.get('explanation', ''))
    st.subheader("Extracted Keywords")
    st.write(", ".join(keywords))