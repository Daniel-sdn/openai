import openai
import os
import json
import time, copy

#openai.api_key = "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"
def transcribe_audio(audio_path):
    since = time.time()    
    openai.api_key = "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"
    with open(audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    texto_transcrib = json.dumps(transcript)
    data = json.loads(texto_transcrib)
    mensagemTranscrita = data['text']
    return mensagemTranscrita 

    

                          