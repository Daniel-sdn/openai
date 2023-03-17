import openai
import os

# Configure a chave de API
openai.api_key = "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"

# Envie uma solicitação de texto para o modelo ChatGPT
response = openai.Completion.create(
  engine="davinci", # Escolha um dos modelos pré-treinados disponíveis
  prompt="Olá, como posso ajudá-lo hoje?",
  max_tokens=60
)

# Imprima a resposta gerada pelo modelo
print(response.choices[0].text)