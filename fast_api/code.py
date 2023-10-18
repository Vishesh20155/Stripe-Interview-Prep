from fastapi import FastAPI
app = FastAPI()

@app.get("/first/{id}")
def hello(id):
  return {f"Hello world!- {id}"}