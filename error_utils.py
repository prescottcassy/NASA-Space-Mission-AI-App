# error_utils.py
"""
Error Utilities for Streamlit NASA App

This module provides reusable functions for handling common errors across the app,
ensuring consistent feedback and user-friendly messages.

Included Functions:
- handle_api_error(error): Displays a red error message for API-related failures.
- handle_model_error(error): Displays a red error for AI model failures with diagnostic output.
- handle_missing_data(message): Shows a yellow warning when expected data is missing.

Usage Example:
    from error_utils import handle_api_error, handle_model_error, handle_missing_data

    try:
        response = requests.get(nasa_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        handle_api_error(e)

Benefits:
- Modular and clean error management
- Enhances user experience inside Streamlit
- Easy to expand with logging or alternative feedback (e.g., toasts, dialogs)

"""

import streamlit as st

def handle_api_error(error):
    st.error(f" API error: {error}")

def handle_model_error(error):
    st.error(" Model failed to generate output.")
    st.text(str(error))

def handle_missing_data(message="Data is missing or incomplete."):
    st.warning(f" {message}")

    from error_utils import handle_api_error, handle_model_error, handle_missing_data

# Example in your fetch function
try:
    response = requests.get(API_URL) # type: ignore
    response.raise_for_status()
except requests.exceptions.RequestException as e: # type: ignore
    handle_api_error(e)

# Example in summarization
try:
    summary = summarize_text(text, summarizer) # type: ignore
except Exception as e:
    handle_model_error(e)

# Check for missing 'explanation' field
if 'explanation' not in data: # type: ignore
    handle_missing_data("No image description available.")