import requests
import json
import base64
import os 
import http.client
import io
from openai import Audio
from pydub import AudioSegment


def send_message(preJid, mensagemTranscrita):
    conn = http.client.HTTPSConnection("api5.megaapi.com.br")

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer MOK9F6yvV9n0EvGIVsuvB7pPBA'
    }

    payload = json.dumps({
      "messageData": {
        "to": "5511994954119@s.whatsapp.net",
        "text": "mensagemTranscrita"
      }
    })

    conn.request("POST", "/rest/sendMessage/megaapi-MOK9F6yvV9n0EvGIVsuvB7pPBA/text", payload, headers)

    res = conn.getresponse()
    data = res.read()  