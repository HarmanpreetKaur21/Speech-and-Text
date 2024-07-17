
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource
)
import httpx
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def deepgram(buffer_data,language):
    # STEP 1 Create a Deepgram client using the API key
    deepgram = DeepgramClient('5da1cbb9a0b27337e1ae7dc141b48c6775912ed2')

    payload: FileSource = {
        "buffer": buffer_data,
    }

    #STEP 2: Configure Deepgram options for audio analysis
    options = PrerecordedOptions(
        model="nova-2",
        smart_format=True,
        language=language,
        diarize=True

    )
    myTimeout = httpx.Timeout(timeout=300, connect=10.0)

    # STEP 3: Call the transcribe_file method with the text payload and options
    response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options,timeout=myTimeout)
    text=response['results']['channels'][0]['alternatives'][0]['paragraphs']['transcript']
    return text

