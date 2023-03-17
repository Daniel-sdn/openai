import requests
import json
import base64
import os 
import http.client
import io
from openai import Audio
from pydub import AudioSegment

def detectarMensagem(data):

    # ---------------- Aqui vai a lógica de parse --------------------------
    messageType = data['messageType']
    
    if messageType == "message.ack":
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
        
    elif messageType == 'audioMessage':
        print()
        print(f"================= {messageType}   ===========================")
        instanceKey = data["instance_key"]
        pushName = data["pushName"]
        mediaKey = data['message']['audioMessage']['mediaKey']
        directPath = data['message']['audioMessage']['directPath']
        url = data['message']['audioMessage']['url']
        mimetype = data['message']['audioMessage']['mimetype']
        tipoMensagem = 'audio'
        print('pushName: ', pushName)
        #print("remoteJid: ",remoteJid)
        print('instancekey: ', instanceKey)
        print()
        print('-------------dados para payload ------------')
        print('mimetype: ', mimetype)
        print('mediaKey: ', mediaKey)
        print('directPath: ', directPath)
        print('url: ', url)
        print('messageType: ', tipoMensagem)
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
        print()
        print("Payload")
        print()
        
        print(payload)
        # Busca audio string base64
        audiString = download_media_message(payload)
        
        # Converte audio string para file ogg
        
        #pathAudio = '/home/dani-boy/openai/audio/audioTeste.ogg'
        #'/home/dani-boy/openai-quickstart-node/Sound/audioTeste.ogg'
        convert_ogg_to_wav(audiString)
        
        
        
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
        
        
        
        

# 1 - Funçao de Busca audio string base64
def download_media_message(payload):
    conn = http.client.HTTPSConnection("api5.megaapi.com.br")

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer MOK9F6yvV9n0EvGIVsuvB7pPBA'
    }

    conn.request("POST", "/rest/instance/downloadMediaMessage/megaapi-MOK9F6yvV9n0EvGIVsuvB7pPBA", payload, headers)

    res = conn.getresponse()
    data = res.read()

    json_str = data.decode("utf-8")
    return json.loads(json_str)
        
# 2 - Funçao de conversao de audio
def convert_ogg_to_wav(json_str, ofn):
    # Assume json_str contains the JSON data with the base64-encoded audio
    json_dict = json.loads(json_str)

    # Decode the base64-encoded audio data
    audio_bytes_str = json_dict['data'].split(',')[1]

    # Convert string to byte-string
    audio_bytes = audio_bytes_str.encode('utf-8')

    with open(ofn, "wb") as f:
        f.write(base64.b64decode(audio_bytes))

    def ogg2wav(ofn):
        wfn = ofn.replace('.ogg','.wav')
        x = AudioSegment.from_file(ofn)
        x.export(wfn, format='wav')

    ogg2wav(ofn)
        