import requests
import json
import base64
import os 
import http.client
import io
import openai
from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
from openai import Audio
from pydub import AudioSegment
import modules.requisicores as req
import modules.workmessage as wkmess
import modules.transcricao as transcr
import time, copy


#import modules.botopenai as bot 


def detectarMensagem(data):
    # ---------------- Aqui vai a lógica de parse --------------------------
    messageType = data['messageType']
    if messageType == 'audioMessage':  # audio message   
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
        
        
        word = "Bia ajude-me"
        biaMessage = "🧑🏼‍🎤Bia: Claro, o que você precisa?"
        
        if word in transcribed_text:
            req.send_message(remoteJid, biaMessage)
            work = "transcreva"
            
            
            os.environ["OPENAI_API_KEY"] = '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'
            MODEL = "gpt-3.5-turbo"
            def ask_ai(valor):
                index = GPTSimpleVectorIndex.load_from_disk('index.json')
                while True: 
                    query = valor
                    response = index.query(query, response_mode="compact")
                    req.send_message(remoteJid, (f"Bia: {response.response}"))
                    break    
             
             
             
             
        # else:
        #     req.send_message(remoteJid, mensagemTranscrita)
        
        transcribed_text
        
        
        textotranscrito = (f'{pushName} peguntou: {transcribed_text}\n')
        
        req.send_message(remoteJid, textotranscrito)
        
        
        

        
        ask_ai(transcribed_text)
        
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
        remoteJid = data['key']['remoteJid']
        fromMe = data['key']['fromMe']
        #status = data['update']['status']
        # Prints
        # print('messageType: ', messageType)
        # print('pushName: ', pushName)
        # print("remoteJid: ",remoteJid)
        # print('instancekey: ', instanceKey)
        # print('broadcast: ', broadcast)
        
        #menssage_text = (f"messageType: {messageType}\nFrom me: {fromMe}\n\nOlá {pushName},  \nMensagem: {mensagem } \n\nDevice: {remoteJid}")
        
        # import openai

        # openai.api_key = "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"
        
        # resposta = bot.ask_ai(mensagem)
        # req.send_message(remoteJid, resposta)
        
        
        import openai

        #openai.api_key = "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"
        
        #os.environ["OPENAI_API_KEY"] = input("Paste your OpenAI key here and hit enter:")
        os.environ["OPENAI_API_KEY"] = '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'

        MODEL = "gpt-3.5-turbo"
                
        def ask_ai(valor):
            index = GPTSimpleVectorIndex.load_from_disk('index.json')
            while True: 
                query = valor
                response = index.query(query, response_mode="compact")
                req.send_message(remoteJid, (f"Bia: {response.response}"))
                break
        
        ask_ai(mensagem)



        
        

        
        
        # resp_bot = bot.ask_ai(mensagem)
        # word = "Pergunta:"
        # if word in mensagem:
        #      resposta = bot.ask_ai(mensagem)
        #      req.send_message(remoteJid, resposta)
                
        # # else:
        # #     req.send_message(remoteJid, mensagemTranscrita)
        
        
        
        # word = "Bia"
        # message = "🧑🏼‍🎤Bia: Olá, posso te ajudar?"
        # if word in mensagemTranscrita:
        #     req.send_message(remoteJid, message)   
        # else:
        #     req.send_message(remoteJid, mensagemTranscrita)
            
        # # # return(mensagemTranscrita) 
        
        #req.send_message(remoteJid, menssage_text)
                
       
        
        
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




        #mensagemTranscrita = wkmess('audioTeste.wav')
        
        # #Transcricao dp audio - whisper openai
        # import openai
        # import os
        # openai.organization = "org-guDH0aNEdRkxo8bOtlGqBstO"
        # openai.api_key = os.getenv("OPENAI_API_KEY")
        # #openai.Model.list()
        


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

