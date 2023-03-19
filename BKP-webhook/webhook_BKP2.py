from urllib import response
from flask import Flask, request, jsonify
import tratamento_bkp3
import json
import requests
import http.client
import time, copy
import modules.requisicores as req
import modules.botopenai as bot 
import modules.transcricao as transc
import modules.botopenai as botai
#import modules.workmessage as 

app = Flask(__name__)



@app.route('/whats', methods=['POST'])
def main():
    since = time.time()
    data = request.get_json(silent=True)
    instanceKey = data["instance_key"]
    messageType = data['messageType']
    fromMe = data['key']['fromMe']
    remoteJid = data['key']['remoteJid'] 
    
    
    
    print()
    print("--------------------------Principais Dados --------------------------")
    print(instanceKey)
    print(remoteJid)
    print(fromMe)
    print(messageType)
    intentWelcome = ['bia, pode me ajudar?','oi bia', 'ola bia', 'olá bia', 'teste', 'menu', 'opções', 'opcoes']
    intentGoodbye = ['obrigado pela ajuada','ate mais', 'fim', 'encerrar', 'obrigado bia']
    message = "🧑🏼‍🎤Bia: Olá, posso te ajudar?"
    
    
    # Assuming `req` is an instance of some request object
    messageBot = "🧑🏼‍🎤Bia: Olá, posso te ajudar?"
    if messageType == 'audioMessage':  # audio message
        while True:
            messagem, name = transc.transcreve_data(data)
            user_input = messagem
            if not botai.ask_ai(user_input, remoteJid):
                req.send_message(remoteJid, "Bia: Goodbye!")
                break  
        # 
        # if messagem.lower() in intentWelcome:
        #     req.send_message(remoteJid, messageBot)
            
        # botai.ask_ai(messagem, remoteJid)
        #     #data = request.get_json(silent=True)
        #     # messagemIter = transc.transcreve_data(data)
        #     # remoteJid = data['key']['remoteJid'] 
        #     # botai.ask_ai(messagemIter, remoteJid)
        #     # if messagem.lower() in intentWelcome:    
            
      
        #menssage_text = (f"{name} perguntou:\n{message}")
        #req.send_message(remoteJid, menssage_text)    

        
        #req.send_message(remoteJid, messagem)
                #Tratamento de intents welcomes

        
        
        
    
    
    
    #if fromMe == True:
    
    #tratamento.detectarMensagem(data) #data
    # chamada da funçao detectarMensagem
    #messageUser = (f"{name} perguntou:\n{message}")
     
    print(f'------------------------------- raw data:  {messageType}  ----------------------------------------')
    
    # print('Volteiiii')
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    print(json_data) 
    # print()
    # print("\n--------------------      eof             -----------------\n")
    # print()
    # print("fechou")
    # print()
    
    return jsonify({})

# run Flask app
if __name__ == "__main__":
    app.debug = True
    app.run()
    


# ngrok config add-authtoken 2KqY2nL5yoztw5bVsDkJZKE4LFn_3Euxa7E22j1iDgXCJ4cyM
# Running on http://127.0.0.1:5000
# ngrok http 5000
# https://mega-api-painel.app.br/megaapi/

#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


# https://github.com/openai/openai-python
 
 
 
 
 #textotranscrito = (f'{pushName} peguntou: {transcribed_text}\n')