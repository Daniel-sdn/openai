import openai
import os
import json
import time, copy

#openai.api_key = "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"
def transcribe_audio(audio_path):
    since = time.time()    
    openai.api_key = "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"
    with open(audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    texto_transcrib = json.dumps(transcript)
    data = json.loads(texto_transcrib)
    mensagemTranscrita = data['text']
    
    #trabalha tempo
    time_elapsed = (time.time() - since) * 1000
    minutes, seconds = divmod(time_elapsed / 1000, 60)
    milliseconds = time_elapsed % 1000
    mensagemTranscritaTempo = (f"\nMensagem: {mensagemTranscrita} \nTempo transcriçao: {minutes:.0f}m {seconds:.0f}s {milliseconds:.0f}ms")
    return mensagemTranscritaTempo 



                # import openai
                # import os
                # openai.api_key = "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"
                # #audio_file = open("/home/dani-boy/openai/audio/teste2-mp3-openai.mp3", "rb")
                # audio_file = open("/home/dani-boy/openai/audio/audioTeste.wav", "rb")
                # transcript = openai.Audio.transcribe("whisper-1", audio_file)
                # #translate = openai.Audio.translate("whisper-1", audio_file)
                # texto_transcrib = json.dumps(transcript)
                # data = json.loads(texto_transcrib)
                # mensagemTranscrita = data['text']
                
                
                
    time_elapsed = time.time() - since
    print(f'\nTraining complete in {time_elapsed // 60:.0f}m {time_elapsed % 60:.0f}s')
    print(f'Best val Acc: {best_acc:4f} at epoch {best_epoch}')                              