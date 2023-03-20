import openai
import os
import json
import time, copy




os.environ["OPENAI_API_KEY"] = input("Paste your OpenAI key here and hit enter:")

# openai.api_key = os.getenv("OPENAI_API_KEY")
# mensagem

def transcribe_audio(audio_path):
    since = time.time()    
    with open(audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    texto_transcrib = json.dumps(transcript)
    data = json.loads(texto_transcrib)
    mensagemTranscrita = data['text']
    return mensagemTranscrita 

    

                          