from urllib import response
from flask import Flask, request, jsonify
import tratamento
import json
import requests
import http.client
import tratamento

app = Flask(__name__)

@app.route('/whats', methods=['POST'])
def main():
    data = request.get_json(silent=True)
    messageType = data['messageType']   
    
    # chamada da funçao detectarMensagem
    tratamento.detectarMensagem(data) #data
     
    print(f'------------------------------- raw data:  {messageType}  ----------------------------------------')
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    print(json_data) 
    print()
    print("\n--------------------      eof             -----------------\n")
    print()
    
    return jsonify({})

# run Flask app
if __name__ == "__main__":
    app.debug = True
    app.run()
    
    
    
