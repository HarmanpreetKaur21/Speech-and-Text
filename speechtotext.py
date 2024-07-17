import streamlit as st
from deepgram import Deepgram
from transcript import deepgram
import urllib3
urllib3.disable_warnings()

def speech_to_text():
    st.title("Speech to Text")

    # File uploader for audio files
    uploaded_file = st.sidebar.file_uploader("Upload Audio File", type=["wav", "mp3"])

    if uploaded_file is not None:
        st.sidebar.audio(uploaded_file, format='audio/wav/mp3')  # Display the uploaded audio file
        st.spinner("Uploading in progress....")
        
       # Language selection dropdown
        options = st.sidebar.selectbox("Select Language", ["English","Hindi"])
        if options=='English':
            language="en"
        elif options=='Hindi':
            language="hi"
    
       

        # Button to trigger transcription
        if st.sidebar.button("Transcribe"):
            with st.spinner("Please Wait,Transcribing in progress..."):
                # Call the transcribe_audio function
                transcript = deepgram(uploaded_file, language)
                with st.container(height=500):
                 st.markdown(transcript)
                
                st.download_button(
                    label="Download Transcribed Text",
                    data=transcript,
                    file_name="transcribed_text.txt",
                    mime="text/plain"
                )                
                
            
    
                 
if __name__ == "__main__":
    speech_to_text()


