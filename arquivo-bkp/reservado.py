# 1 - Funçao de Busca audio string base64
def download_media_message(payload):
    conn = http.client.HTTPSConnection("api5.megaapi.com.br")

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer MOK9F6yvV9n0EvGIVsuvB7pPBA'
    }

    conn.request("POST", "/rest/instance/downloadMediaMessage/megaapi-MOK9F6yvV9n0EvGIVsuvB7pPBA", payload, headers)

    res = conn.getresponse()
    data = res.read()

    json_str = data.decode("utf-8")
    return json.loads(json_str)
        
# 2 - Funçao de conversao de audio
def convert_ogg_to_wav(json_str):
    # Assume json_str contains the JSON data with the base64-encoded audio
    json_dict = json.loads(json_str)

    # Decode the base64-encoded audio data
    audio_bytes_str = json_dict['data'].split(',')[1]

    # Convert string to byte-string
    audio_bytes = audio_bytes_str.encode('utf-8')

    with open('/home/dani-boy/openai/audio/audioTeste.ogg', "wb") as f:
        f.write(base64.b64decode(audio_bytes))

    def ogg2wav(ofn):
        wfn = ofn.replace('.ogg','.wav')
        x = AudioSegment.from_file(ofn)
        x.export(wfn, format='wav')

    ogg2wav('/home/dani-boy/openai/audio/audioTeste.ogg')
        