import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer
from torch import embedding


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# EMbedding has its own model
model = SentenceTransformer("all-MiniLM-L6-v2")  # 384 vector size

text = "Machine learning is fun"

# embedding = model.encode(text)
# print(embedding.shape)
# print(embedding[:10])

t1 = "there are 24 paid leaves"
t2 = "I love pizza"

vector1 = model.encode(t1)
vector2 = model.encode(t2)

print(cosine_similarity(vector1, vector2))
