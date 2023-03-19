import requests
import json
import base64
import os 
import http.client
import io
from openai import Audio
from pydub import AudioSegment

#preJid = '5511994954119@s.whatsapp.net'

#mensagemTranscrita = 'Reseres'


def send_message(destinatario, mensagem):
    conn = http.client.HTTPSConnection("api5.megaapi.com.br")

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer MOK9F6yvV9n0EvGIVsuvB7pPBA'
    }

    payload = json.dumps({
      "messageData": {
        "to": destinatario,
        "text": mensagem
      }
    })

    conn.request("POST", "/rest/sendMessage/megaapi-MOK9F6yvV9n0EvGIVsuvB7pPBA/text", payload, headers)

    res = conn.getresponse()
    data = res.read()  
    

    
    
