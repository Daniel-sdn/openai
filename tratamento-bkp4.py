import requests
import json
import base64
import os 
import http.client
import io
from openai import Audio
from pydub import AudioSegment
import modules.requisicores as req
import modules.workmessage as wkmess
import time, copy
from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import openai
#import modules.botopenai as bot

#openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = input("Paste your OpenAI key here and hit enter:")

MODEL = "gpt-3.5-turbo"

def detectarMensagem(data):
    pushName = data["pushName"]
    remoteJid = data['key']['remoteJid'] 
    messageType = data['messageType']
    if messageType == 'audioMessage':  # audio message   
        instanceKey = data["instance_key"]     
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
        audio_path = "/home/dani-boy/openai/audio/audioTeste.wav"
        transcribed_text = wkmess.transcribe_audio(audio_path)
        textotranscrito = (f'{pushName} peguntou: {transcribed_text}\n')
        req.send_message(remoteJid, textotranscrito)
        ask_ai(transcribed_text)
             
    elif messageType == 'conversation':
        print()
        print(f"=================  {messageType}   ===========================")
        pushName = data["pushName"]
        mensagem = data['message']['conversation']
        broadcast = data['broadcast']
        remoteJid = data['key']['remoteJid']
        fromMe = data['key']['fromMe']
        
        # openai.api_key = os.getenv("OPENAI_API_KEY")
        # os.environ["OPENAI_API_KEY"] = input("Paste your OpenAI key here and hit enter:")
        ask_ai(mensagem)
    
    elif messageType == "message.ack":
        def ask_ai(valor):
            index = GPTSimpleVectorIndex.load_from_disk('index.json')
            while True: 
                query = valor
                response = index.query(query, response_mode="compact")
                req.send_message(remoteJid, (f"🧑🏼‍🎤 Bia: {response.response}"))
                break
        instanceKey = data["instance_key"]
        jid = data['jid']
        messageType = data['messageType']
        remoteJid = data['key']['remoteJid']
        id = data['key']['id']
        fromMe = data['key']['fromMe']        
        ask_ai(mensagem)     
        
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

    def ask_ai(valor):
        index = GPTSimpleVectorIndex.load_from_disk('index.json')
        while True: 
            query = valor
            response = index.query(query, response_mode="compact")
            req.send_message(remoteJid, (f"🧑🏼‍🎤 Bia: {response.response}"))
            break



def set_name(name):
    conn = http.client.HTTPSConnection("api5.megaapi.com.br")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer MOK9F6yvV9n0EvGIVsuvB7pPBA'
    }
    payload = json.dumps({
                "messageData": {
                "name": name
                }
    })
    conn.request("POST", "/rest/instance/setProfileName/megaapi-MOK9F6yvV9n0EvGIVsuvB7pPBA/text", payload, headers)
    
    # res = conn.raise_for_status()
    # print(res.json())
    
    
def set_presence(preJid, status):
    conn = http.client.HTTPSConnection("api5.megaapi.com.br")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer MOK9F6yvV9n0EvGIVsuvB7pPBA'
    }
    
    payload = json.dumps({
      "messageData": {
        "to": preJid,
        "option": status
      }
    })
    conn.request("POST", "/rest/chat/megaapi-MOK9F6yvV9n0EvGIVsuvB7pPBA/presenceUpdateChat", payload, headers)
    res = conn.getresponse()
    data = res.read()    



        
intentWelcome = ['bia, pode me ajudar?','oi bia', 'ola bia', 'olá bia', 'teste', 'menu', 'opções', 'opcoes']
intentGoodbye = ['obrigado pela ajuada','ate mais', 'fim', 'encerrar', 'obrigado bia']
message = "🧑🏼‍🎤Bia: Olá, posso te ajudar?"       




        #req.send_message(remoteJid, transcribed_text)
        
        #send_message(remoteJid, mensagemTranscrita)
        # set_name("Peter")
        # option = "composing"
        # set_presence(remoteJid, option)
        #return remoteJid, mensagemTranscrita 
        #send_message(remoteJid, mensagemTranscrita)
                        
        # word = "Bia"
        # message = "🧑🏼‍🎤Bia: Olá, posso te ajudar?"
        # if word in mensagemTranscrita:
        #     req.send_message(remoteJid, message)   
        # else:
        #     req.send_message(remoteJid, mensagemTranscrita)
            
        # # # return(mensagemTranscrita)    

# import openai
# import json

# def transcribe_audio(audio_path):
#     openai.api_key = "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"
#     with open(audio_path, "rb") as audio_file:
#         transcript = openai.Audio.transcribe("whisper-1", audio_file)
#     texto_transcrib = json.dumps(transcript)
#     data = json.loads(texto_transcrib)
#     mensagemTranscrita = data['text']
#     return mensagemTranscrita

        #status = data['update']['status']
        # Prints
        # print('messageType: ', messageType)
        # print('pushName: ', pushName)
        # print("remoteJid: ",remoteJid)
        # print('instancekey: ', instanceKey)
        # print('broadcast: ', broadcast)
        
        #menssage_text = (f"messageType: {messageType}\nFrom me: {fromMe}\n\nOlá {pushName},  \nMensagem: {mensagem } \n\nDevice: {remoteJid}")
        #mensagemTranscrita = wkmess('audioTeste.wav')
        # #Transcricao dp audio - whisper openai
        # import openai
        # import os
        # openai.organization = "org-guDH0aNEdRkxo8bOtlGqBstO"
        # openai.api_key = os.getenv("OPENAI_API_KEY")
        # #openai.Model.list()
     
# def send_message(preJid, mensagemTranscrita):
#     conn = http.client.HTTPSConnection("api5.megaapi.com.br")

#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Bearer MOK9F6yvV9n0EvGIVsuvB7pPBA'
#     }

#     payload = json.dumps({
#       "messageData": {
#         "to": preJid,
#         "text": mensagemTranscrita
#       }
#     })

#     conn.request("POST", "/rest/sendMessage/megaapi-MOK9F6yvV9n0EvGIVsuvB7pPBA/text", payload, headers)

#     res = conn.getresponse()
#     data = res.read()        
        
        
# import openai

# openai.api_key = "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"

# MODEL = "gpt-3.5-turbo"        
        
        
# # An example of a system message that primes the assistant to explain concepts in great depth
# response = openai.ChatCompletion.create(
#     model=MODEL,
#     messages=[
#         {"role": "system", "content": "Você ensina crianças de ate 6 anos."},
#         {"role": "user", "content": "O que sao frações?"},
#     ],
#     temperature=0.5,
# )

# print(response["choices"][0]["message"]["content"])        
 