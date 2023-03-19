from urllib import response
from flask import Flask, request, jsonify
import tratamento_evoluindo
import json
import requests
import http.client
import tratamento_evoluindo
import time, copy

app = Flask(__name__)

@app.route('/whats', methods=['POST'])
def main():
    since = time.time()
    data = request.get_json(silent=True)
    messageType = data['messageType'] 
    fromMe = data['key']['fromMe']  
 
    if fromMe == True:
        tratamento_evoluindo.detectarMensagem(data) #data
    # chamada da funçao detectarMensagem
    
     
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
 