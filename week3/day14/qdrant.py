import os
from dotenv import load_dotenv
from groq import Groq
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import numpy as np
from sentence_transformers import SentenceTransformer
from torch import embedding

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Load variable from .env
load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Connect to QDRANT

client = QdrantClient(api_key=QDRANT_API_KEY, url=QDRANT_URL)
print("Connected to Qdrant cloud")

# create COLLECTION in QDRANT

COLLECTION_NAME = "knowledge"
EMBEDDING_SIZE = 384

if client.collection_exists(COLLECTION_NAME):
    print(f"Deleting exsisting collection: {COLLECTION_NAME}")
    client.delete_collection(COLLECTION_NAME)

client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=EMBEDDING_SIZE, distance=Distance.COSINE),
)

print(f"Created Collection: {COLLECTION_NAME}")
print(f"Vector Size: {EMBEDDING_SIZE}")
print("Distance: Cosine")


# LOAD OUR KNOWLEDGE

with open("knowledge.txt", "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f if line.strip()]
# [line1, line2, line3 ...]
print(f"Loaded {len(documents)} documents")

# CREATE EMBEDDING
print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("EMbedding model ready!")

embeddings = model.encode(documents)

print(f"Generated {len(embeddings)} embeddings")
print(f"Embedding size: {len(embeddings[0])}")


# Create QDRANT POINTS
points = []
for i, embedding in enumerate(embeddings):

    point = PointStruct(
        id=i + 1, vector=embedding.tolist(), payload={"text": documents[i]}
    )
    points.append(point)

# upload to QDRANT

client.upsert(collection_name=COLLECTION_NAME, points=points)
print(f"Uploaded {len(points)} documents to Qdrant")


# search QDRANT


def search(query, top_k=3):

    # convert question into embedding
    query_vector = model.encode(query)

    # search Qdranr for similar vectors
    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k,
        with_payload=True,
    ).points

    return results


# TEST SEARCH

query = "how many vacations day do I get"
results = search(query, top_k=3)

print("\nSearch results:")

for result in results:
    print(f"Score: {result.score: .3f}")
    print(result.payload["text"])
    print()

# Connect to groq
if not GROQ_API_KEY:
    raise ValueError("api error")

groq_client = Groq(api_key=GROQ_API_KEY)
grok_model = "qwen/qwen3.8-27b"


def ask_llm(context, question):
    system_prompt = f"""answer in one line only. and answer only based on this context {context}. do not hallucinate.
    if answer not present in the context. say I dont know based on the information provided."""
    system_message = {"role": "system", "content": system_prompt}
    message = {"role": "user", "content": question}
    messages = [system_message, message]
    response = groq_client.chat.completions.create(model=grok_model, messages=messages)
    answer = response.choices[0].message.content
    return answer


# complete RAG pipelinr

question = "how many vacations do i get?"

results = search(question, top_k=3)

context = "\n".join(result.payload["text"] for result in results)

print(context)

answer = ask_llm(context, question)

print("\nFinal Answer:")
print(answer)
