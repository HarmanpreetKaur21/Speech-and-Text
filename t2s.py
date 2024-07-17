import streamlit as st
from gtts import gTTS
import os

# Function to save the speech to a file using gTTS
def save_speech(text, lang, filename):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

# Function to run the Streamlit app
def text_to_speech_page():
    st.title("Text-to-Speech")

    # Dropdown to select language
    language = st.selectbox("Select Language", ["English", "Hindi"])

    # Text input for the user to enter text
    text_input = st.text_area("Enter text to convert to speech", "")

    # Button to trigger TTS
    if st.button("Convert to Speech"):
        if text_input:
            # Map the selected language to gTTS language codes
            lang_code = 'en'
            if language == "Hindi":
                lang_code = 'hi'
            

            # Save the speech to an audio file
            output_audio_file = "output.mp3"
            save_speech(text_input, lang_code, output_audio_file)

            # Play the audio file
            st.audio(output_audio_file, format='audio/mp3')
        else:
            st.warning("Please enter some text to convert.")

# Run the app
if __name__ == "__main__":
    text_to_speech_page()
