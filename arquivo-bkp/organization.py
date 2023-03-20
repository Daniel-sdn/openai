import os
import openai
openai.organization = "org-guDH0aNEdRkxo8bOtlGqBstO"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()