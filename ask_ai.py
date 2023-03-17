from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import sys
import os
from IPython.display import Markdown, display


import openai
os.environ["OPENAI_API_KEY"] = input("Paste your OpenAI key here and hit enter:")

def ask_ai():
    #openai.api_key = "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"
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while True: 
        query = input("Como posso te ajudar? ")
        response = index.query(query, response_mode="compact")
        display(Markdown(f"Samantha: <b>{response.response}</b>"))