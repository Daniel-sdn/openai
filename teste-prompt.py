
import openai

openai.api_key = "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"

MODEL = "gpt-3.5-turbo"

# Example OpenAI Python library request
MODEL = "gpt-3.5-turbo"
response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": "Quem foi Leonardo da Vinci?"},
        {"role": "assistant", "content": "Sobre qual aspecto?"},
        {"role": "user", "content": "Pintor."},
    ],
    temperature=0,
)

print(response)