import requests
import json
import base64
import os 
import http.client
import io
from openai import Audio
from pydub import AudioSegment

def detectarMensagem(data, type):
    # ---------------- Aqui vai a lógica de parse --------------------------
    if messageType == 'conversation':  #=================  {messageType}   ===========================")
        print()
        pushName = data["pushName"]
        mensagem = data['message']['conversation']
        broadcast = data['broadcast']
        remoteJid = data['key']['remoteJid']
        #status = data['update']['status']
        # Prints
        # print('messageType: ', messageType)
        # print('pushName: ', pushName)
        # print("remoteJid: ",remoteJid)
        # print('instancekey: ', instanceKey)
        # print('broadcast: ', broadcast)
        # print('status: ', status)
        # print('mensagem: ', mensagem)
        #return(remoteJid, mensagem) 
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
        
        
def send_message(preJid, mensagemTranscrita):
    conn = http.client.HTTPSConnection("api5.megaapi.com.br")

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer MOK9F6yvV9n0EvGIVsuvB7pPBA'
    }

    payload = json.dumps({
      "messageData": {
        "to": preJid,
        "text": mensagemTranscrita
      }
    })

    conn.request("POST", "/rest/sendMessage/megaapi-MOK9F6yvV9n0EvGIVsuvB7pPBA/text", payload, headers)

    res = conn.getresponse()
    data = res.read()        
        
        
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

