# Speech-and-Text
This project mainly contains two parts-- 
1)Speech to text
The deepgram Api key is used to make speech to text part of the project. User inputs the audio to transcribe it into text. The transcribed text can be downloaded in the .txt file. It supports both English and Hindi language.
2)Text to speech
The gtts library is used for this task. User inputs the text and can convert it into the audio. The audio file can also be easily downloaded. It also supports both English and Hindi language.

## Installation

To get started with the project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/HarmanpreetKaur21/Speech-and-Text.git
    ```

2. Navigate to the project directory:
    ```sh
    cd Speech-and-Text
    ```

3. Install the required dependencies:
    ```sh
    pip install streamlit
    pip install gtts
    pip install deepgram-sdk
    ```

## Usage

To run the project:

1. Download all the files and save them in a folder.

2. Open the folder in VS Code:
    
3. Run the project using Streamlit:
    ```sh
    streamlit run app.py
    ```

4. Follow the instructions in the Streamlit interface to use the speech-to-text and text-to-speech functionalities.

## Features

- Converts speech to text
- Converts text to speech
- User-friendly interface using Streamlit
- Integrates with Deepgram SDK for advanced speech processing

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request
