import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer

os.environ["TOKENIZERS_PARALLELISM"] = "false"

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client = Groq(api_key=my_api_key)
grok_model = "qwen/qwen3.8-27b"

# EMbedding has its own model
model = SentenceTransformer("all-MiniLM-L6-v2")  # 384 vector size


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# knowledge base
documents = [
    "Employee receive 24 days of paid leave per year.",
    "Employee work from the office on Tuesday, Wednesday and Thursday",
    "Employees have a 90 day notice period",
]

# Made vector for each line of knowledge base (array)
document_embeddings = model.encode(documents)


# We will call similarity between query and document embedding and then send the top element as a context bcoz that would
# be most relevant to our query


def retrieve(qembedding):
    scores = []
    for i, document in enumerate(document_embeddings):
        score = cosine_similarity(qembedding, document)
        scores.append((score, documents[i]))
    scores.sort(reverse=True)
    return scores[0]


def ask_llm(context, question):
    system_prompt = f"""answer in one line only. and answer only based on this context {context}. do not hallucinate"""
    system_message = {"role": "system", "content": system_prompt}
    message = {"role": "user", "content": question}
    messages = [system_message, message]
    response = client.chat.completions.create(model=grok_model, messages=messages)
    answer = response.choices[0].message.content
    return answer


query = "how much vacation do I get?"
qembedding = model.encode(query)


score, context = retrieve(qembedding)
print(score)
print(context)
print(ask_llm(context, query))


# Retrieval -> find out best data from knowledge base using embedding
# Augmented -> reading that retrieval context and giving answer is task of llm
# Generation -> output generated after above 2
