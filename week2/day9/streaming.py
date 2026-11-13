import os
from pathlib import Path
from pyexpat.errors import messages
from turtle import mode
from urllib import response
from dotenv import load_dotenv
from groq import Groq
import re
from time import sleep

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client = Groq(api_key=my_api_key)
model = "qwen/qwen3.8-27b"

prompt = "Explain how internet works."
message = {"role": "user", "content": prompt}

messages = [message]

# response = client.chat.completions.create(model=model, messages=messages)
# # print(response)
# answer = response.choices[0].message.content
# print(answer)

stream = client.chat.completions.create(model=model, messages=messages, stream=True)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(
            content, end="", flush=True
        )  # flush true means jese jese answer ata jaye hume print chayeye
