import openai
import os
import json

openai.api_key = "sk-...I"
audio_file = open("/home/dani-boy/openai/audio/audioTeste.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
texto_transcrib = json.dumps(transcript)
data = json.loads(texto_transcrib)
mensagemTranscrita = data['text']