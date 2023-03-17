from urllib import response
from flask import Flask, request, jsonify
import tratamento
import json
import requests
import http.client
import tratamento
import transcricao

app = Flask(__name__)

@app.route('/whats', methods=['POST'])
def main():
    data = request.get_json(silent=True)
    messageType = data['messageType']  
    print(messageType)
    if messageType == 'conversation':
        tratamento.detectarMensagem(data, type=messageType)
        transcricao.transcreve_data(data) #data
    elif messageType == 'video':
        tratamento.detectarMensagem(data)    
    
    
    # chamada da funçao detectarMensagem
     
    print(f'------------------------------- raw data:  {messageType}  ----------------------------------------')
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    print(json_data) 
    print("\n--------------------      eof             -----------------\n")
    print()
    
    return jsonify({})

# run Flask app
if __name__ == "__main__":
    app.debug = True
    app.run()
    
    
    
