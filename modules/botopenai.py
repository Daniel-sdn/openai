from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import sys
import os
from IPython.display import Markdown, display
import modules.requisicores as req

import openai


#openai.api_key = "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"
        
#os.environ["OPENAI_API_KEY"] = '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'

openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-3.5-turbo"    

intentGoodbye = ['obrigado pela ajuda', 'ate mais', 'fim', 'encerrar', 'obrigado bia']    

def ask_ai(valor, remoteJid):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    query = valor
    response = index.query(query, response_mode="compact")
    if any(word in response.response for word in intentGoodbye):
        return False
    req.send_message(remoteJid, f"Bia: {response.response}")
    return True


# def ask_ai(valor, remoteJid):
#     index = GPTSimpleVectorIndex.load_from_disk('index.json')
#     while True:   
#         query = valor
#         response = index.query(query, response_mode="compact")
#         req.send_message(remoteJid, (f"Bia: {response.response}"))
#         if any(word in response.response for word in intentGoodbye):
#             break
      
        
# def ask_ai(valor, remoteJid):
#     index = GPTSimpleVectorIndex.load_from_disk('index.json')
#     while True:   
#         query = valor
#         response = index.query(query, response_mode="compact")
#         req.send_message(remoteJid, (f"Bia: {response.response}"))
#         break
    
        # if response2.lower() in intentGoodbye:
        #     messageBot = "🧑🏼‍🎤Bia: Estou aqui sempre que precisar, ate mais"
        #     req.send_message(remoteJid, (f"Bia: {messageBot}")) 
        
        
        
# intentGoodbye = ['obrigado pela ajuada','ate mais', 'fim', 'encerrar', 'obrigado bia']        
# def ask_ai(valor, remoteJid):
#     index = GPTSimpleVectorIndex.load_from_disk('index.json')
#     while True:   
#         query = valor
#         response = index.query(query, response_mode="compact")
#         if any(word in response.response for word in intentGoodbye):
#             break
#         req.send_message(remoteJid, (f"Bia: {response.response}"))        
               
            