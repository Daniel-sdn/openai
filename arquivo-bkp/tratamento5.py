import requests
import json
import base64
import os 
import http.client
import io
from openai import Audio
from pydub import AudioSegment
import openai


def detectarMensagem(data):

    # ---------------- Aqui vai a lógica de parse --------------------------
    messageType = data['messageType']
    if messageType == 'audioMessage':
        print(f"================= {messageType}   ===========================")
        #instanceKey = data["instance_key"]
        pushName = data["pushName"]
        remoteJid = data['key']['remoteJid']
        mediaKey = data['message']['audioMessage']['mediaKey']
        directPath = data['message']['audioMessage']['directPath']
        url = data['message']['audioMessage']['url']
        mimetype = data['message']['audioMessage']['mimetype']
        tipoMensagem = 'audio'
        # print('pushName: ', pushName)
        # print("remoteJid: ",remoteJid)
        # print('instancekey: ', instanceKey)
        # print()
        # print('-------------dados para payload ------------')
        # print('mimetype: ', mimetype)
        # print('mediaKey: ', mediaKey)
        # print('directPath: ', directPath)
        # print('url: ', url)
        # print('messageType: ', tipoMensagem)
        #cria payload para request    
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
        #payload = json.dumps(payloadString, indent=4, ensure_ascii=False)
        # Assume json_str contains the JSON data with the base64-encoded audio
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
        openai.api_key = "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"
        #audio_file = open("/home/dani-boy/openai/audio/teste2-mp3-openai.mp3", "rb")
        audio_file = open("/home/dani-boy/openai/audio/audioTeste.wav", "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        #translate = openai.Audio.translate("whisper-1", audio_file)
        texto_transcrib = json.dumps(transcript)
        data = json.loads(texto_transcrib)
        mensagemTranscrita = data['text']
        payload = json.dumps({
        "messageData": {
            "to": remoteJid,
            "text": mensagemTranscrita
            }
        })

        conn.request("POST", "/rest/sendMessage/megaapi-MOK9F6yvV9n0EvGIVsuvB7pPBA/text", payload, headers)
        res = conn.getresponse()
        data = res.read()
        
    elif messageType == "message.ack":
        instanceKey = data["instance_key"]
        jid = data['jid']
        messageType = data['messageType']
        remoteJid = data['key']['remoteJid']
        id = data['key']['id']
        fromMe = data['key']['fromMe']
        # print(f"================= {messageType}   ===========================")
        # print(f'instanceKey: {instanceKey}')
        # print(f'jid: {jid}')
        # print(f'messageType: {messageType}')
        # print(f'remoteJid: {remoteJid}')
        # print(f'id: {id}')
        # print(f'fromMe: {fromMe}') 
             
    elif messageType == 'conversation':
        print()
        print(f"=================  {messageType}   ===========================")
        pushName = data["pushName"]
        mensagem = data['message']['conversation']
        broadcast = data['broadcast']
        #status = data['update']['status']
        # Prints
        # print('messageType: ', messageType)
        # print('pushName: ', pushName)
        # print("remoteJid: ",remoteJid)
        # print('instancekey: ', instanceKey)
        # print('broadcast: ', broadcast)
        # print('status: ', status)
        # print('mensagem: ', mensagem)
        
    elif messageType == 'imageMessage':
        print()
        print(f"=================  {messageType}   ===========================")
        instanceKey = data["instance_key"]
        jid = data['jid']
        messageType = data['messageType']
        #KEY
        remoteJid = data['key']['remoteJid']
        fromMe = data['key']['fromMe']
        id = data['key']['id']
        participant = data['key']['participant']
        #Back to DATA
        messageTimestamp = data['messageTimestamp']
        pushName = data['pushName']
        broadcast = data['broadcast']
        
        
        
        
