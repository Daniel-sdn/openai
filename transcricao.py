import requests
import json
import base64
import os 
import http.client
import io
from openai import Audio
from pydub import AudioSegment

def transcreve_data(data):
    instanceKey = data["instance_key"]
    pushName = data["pushName"]
    remoteJid = data['key']['remoteJid']
    mediaKey = data['message']['audioMessage']['mediaKey']
    directPath = data['message']['audioMessage']['directPath']
    url = data['message']['audioMessage']['url']
    mimetype = data['message']['audioMessage']['mimetype']
    tipoMensagem = 'audio'
    payload = json.dumps({
        "messageKeys": {
        "mediaKey": mediaKey,
        "directPath": directPath,
        "url": url,
        "mimetype": mimetype,
        "messageType": tipoMensagem
        }
    })
    #Busca string audio
    conn = http.client.HTTPSConnection("api5.megaapi.com.br")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer MOK9F6yvV9n0EvGIVsuvB7pPBA'
    }
    conn.request("POST", "/rest/instance/downloadMediaMessage/megaapi-MOK9F6yvV9n0EvGIVsuvB7pPBA", payload, headers)  
    res = conn.getresponse()
    data = res.read()
    json_str = data.decode("utf-8")
    json_dict = json.loads(json_str)
    # Decode the base64-encoded audio data
    audio_bytes_str = json_dict['data'].split(',')[1]
    # Convert string to byte-string
    audio_bytes = audio_bytes_str.encode('utf-8')
    # Assume json_str contains the JSON data with the base64-encoded audio
    json_dict = json.loads(json_str)
    # Decode the base64-encoded audio data
    audio_str = json_dict['data'].split(',')[1]
    with open('/home/dani-boy/openai/audio/audioTeste.ogg', "wb") as f:
        f.write(base64.b64decode(audio_bytes))
    
    def ogg2wav(ofn):
        wfn = ofn.replace('.ogg','.wav')
        x = AudioSegment.from_file(ofn)
        x.export(wfn, format='wav') 
    ogg2wav('/home/dani-boy/openai/audio/audioTeste.ogg')       
    #Transcricao dp audio - whisper openai
    import openai
    openai.api_key = "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"
    #audio_file = open("/home/dani-boy/openai/audio/teste2-mp3-openai.mp3", "rb")
    audio_file = open("/home/dani-boy/openai/audio/audioTeste.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    #translate = openai.Audio.translate("whisper-1", audio_file)
    texto_transcrib = json.dumps(transcript)
    data = json.loads(texto_transcrib)
    mensagemTranscrita = data['text']


