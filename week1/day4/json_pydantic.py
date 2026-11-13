from email import message
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"
role = "user"
text = (
    "Hello My name is Ayush. I have an iphone which is not working at all. My address is Delhi. my email is abc@gmail.com"
    "My contact number is 82122"
)
prompt = f"""
This is a customer ticket. Please extract the personal information from this {text}
"""

from pydantic import BaseModel


class Ticket(BaseModel):
    name: str
    email: str
    issue: str


schema = Ticket.model_json_schema()

response_format = {"type": "json_object"}

system_prompt = f"""
Extract the personal information from the ticket strictly based on this schema {schema} and give json output
"""
message_system = {"role": "system", "content": system_prompt}

message = {"role": "user", "content": prompt}

# first pass message system
messages = [message_system, message]

response = client.chat.completions.create(
    model=model, messages=messages, response_format=response_format
)
answer = response.choices[0].message.content
print(answer)

import json

raw_json = answer
data_file = json.loads(raw_json)

ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
