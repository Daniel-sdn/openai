import requests
import json
import base64
import os 

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
        
        
        
    elif messageType == 'conversation':
        print()
        print(f"=================  {messageType}   ===========================")
        pushName = data["pushName"]
        mensagem = data['message']['conversation']
        broadcast = data['broadcast']
        status = data['update']['status']
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
        
        