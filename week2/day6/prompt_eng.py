import os
from pathlib import Path
from urllib import response
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-20b"


def llm_ans(prompt):
    message = {"role": "user", "content": prompt}

    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages)
    ans = response.choices[0].message.content
    return ans


bad_prompt = """
This is a user complaint:
My girlfriend not working
Classify this
"""
good_prompt = """
#Role:
You are a support assistant at a mobile/laptop company
#Task:
You have to classify the issue in a category
#CONSTRAINT:
you have to classify the issue in one of the three categories named billing, technical, return
#OUTPUT FORMAT
your answer should be in one word only and your one word should be one of the categories given in the constraints
#ZERO/ONE SHOT
For Instance if a user complains says he want a refund then category is Return
#Fallback
if the issue is not related to any of the categories mentioned in the constaints, then the answer should be OTHER
This is a user complaint:
My laptop is not working
Classify this
"""

print(llm_ans(good_prompt))
