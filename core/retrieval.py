import faiss
import numpy as np
from openai import OpenAI

client = OpenAI()

rules = open("rules/corep_rules.txt").read().split("\n")

def embed(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return np.array(response.data[0].embedding, dtype="float32")

vectors = [embed(rule) for rule in rules if rule.strip() != ""]
index = faiss.IndexFlatL2(len(vectors[0]))
index.add(np.array(vectors))

clean_rules = [r for r in rules if r.strip() != ""]

def retrieve_rules(query):
    query_vec = embed(query)
    D, I = index.search(np.array([query_vec]), k=3)
    return [clean_rules[i] for i in I[0]]
