# NASA-Space-Mission-AI-Project - Implementation Track by Cassy Cormier
July 19th, 2025
Artificial Intelligence Applications Course

## Project Overview
This AI-powered app automatically retrieves and summarizes recent space imagery from NASA’s Astronomy Picture of the Day API. Using natural language processing (NLP), it generates concise captions and keyword tags for each photo—enhancing accessibility and insight across NASA’s expanding visual archives.

## Table of Contents
│
├── README.md           # Project documentation
├── requirements.txt    # Project dependencies
├── my_app.py           # Main app file
├── error_utils.py      # Basic error handling
└── keyword_tools.py    # Keyword extraction

## Tech Stack Summary
-Data API: NASSA Astronomy API
-NLP: Hugging Face Transformers
-Keyword Extractor: spaCY
-User Interface: Streamlit
-Language: Python

## How to run this code
1. Clone the repository
2. Create a Virtual Environment (Recommended)
3. Install Dependencies (requirements.txt)
4. Get a NASA APOD API Key for free
5. (Optional) Create a .env File
6. Launch the Streamlit App using your broswer by running this code in your terminal: python -m streamlit run my_app.py