from fastapi import FastAPI
from pydantic import BaseModel
from scraper import scrape_docs
from vector_store import vector_store
import openai

openai.api_key = "dummy"

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "CDP Chatbot is running!"}

@app.post("/ask")
def ask_cdp(query: QueryRequest):
    results = vector_store.search(query.query)
    context = "\n\n".join([r['content'][:1000] for r in results])  # Limit text to avoid token overflow

    completion = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You're a chatbot assisting with CDP queries."},
                  {"role": "user", "content": f"Answer using this context: {context} \n\n {query.query}"}]
    )
    return {"response": completion["choices"][0]["message"]["content"]}

@app.on_event("startup")
def load_docs():
    docs = scrape_docs()
    vector_store.add_documents(docs)
