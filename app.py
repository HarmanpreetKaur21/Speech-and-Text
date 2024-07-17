import streamlit as st
from  speechtotext import speech_to_text
from t2s import text_to_speech_page

def main():
    st.title("Speak n Text")

    # Define a dictionary to map page names to their corresponding functions
    pages = {
        "Text to Speech": text_to_speech_page,
        "Speech to Text": speech_to_text
    }

    # Display a sidebar for navigation
    st.sidebar.title("Navigation")

    # Get the selection from the user
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    # If the user selects "Text to Speech", show the text-to-speech page
    if selection == "Text to Speech":
        text_to_speech_page()

    # If the user selects "Speech to Text", show the speech-to-text page
    elif selection == "Speech to Text":
        speech_to_text()

    # Add additional pages here as needed
    # elif selection == "Page Name":
    #     page_function()

if __name__ == "__main__":
    main()
