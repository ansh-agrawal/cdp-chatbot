import faiss
import numpy as np
import openai

openai.api_key = "dummy"

class VectorStore:
    def __init__(self):
        self.index = faiss.IndexFlatL2(1536)  # OpenAI Embedding Dimension
        self.documents = []

    def embed_text(self, text):
        response = openai.Embedding.create(input=[text], model="text-embedding-ada-002")
        return np.array(response['data'][0]['embedding'], dtype=np.float32)

    def add_documents(self, docs):
        for doc in docs:
            embedding = self.embed_text(doc['content'])
            self.index.add(np.array([embedding]))  
            self.documents.append(doc)

    def search(self, query, top_k=2):
        query_embedding = self.embed_text(query).reshape(1, -1)
        _, indices = self.index.search(query_embedding, top_k)
        return [self.documents[i] for i in indices[0]]

vector_store = VectorStore()
