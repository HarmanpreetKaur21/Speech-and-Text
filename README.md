# Speech-and-Text
This project mainly contains two parts-- 
1)Speech to text
The deepgram Api key is used to make speech to text part of the project. User inputs the audio to transcribe it into text. The transcribed text can be downloaded in the .txt file. It supports both English and Hindi language.
2)Text to speech
The gtts library is used for this task. User inputs the text and can convert it into the audio. The audio file can also be easily downloaded. It also supports both English and Hindi language.

# To run the project
Download all the files and save it in a folder. Open the folder in the vs code.
Download the required requirements using-
pip install streamlit
pip install gtts
pip install deepgram-sdk
Run the project using
streamlit run app.py
