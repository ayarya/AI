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
model = "qwen/qwen3.8-27b"

# step 1
knowledge_base = {
    "age": "The age of Ayush is 30 years",
    "net_worth": "The net worth of Ayush is 20",
}


# step 2.   //// Very rigid software and can answer based on just keyword age if it ask for any person age
# THIS WAS FIRST ITERATION OF RAG BUT IT WAS CONCEPT THEN AFTER THIS DIFFERENT THINGS COME UP
def retrieve_info(question):
    question = question.lower()
    if "age" in question:
        return knowledge_base["age"]
    elif "net worth" in question:
        return knowledge_base["net_worth"]
    else:
        return None


def ask_llm(question):
    context = retrieve_info(question)

    system_prompt = f"""answer in one line only. and answer only based on this context {context}. do not hallucinate"""
    system_message = {"role": "system", "content": system_prompt}
    message = {"role": "user", "content": question}
    messages = [system_message, message]
    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    return answer


question = "what is age of  ayush?"
question2 = "how rich is Ayush?"
question3 = "how old is ayush"
print(ask_llm(question))
print(ask_llm(question2))
print(ask_llm(question3))
