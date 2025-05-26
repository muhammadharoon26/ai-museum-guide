from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.rag_agent import get_agent
from app.guardrails import is_safe_query

app=FastAPI()
agent=get_agent()

class QueryRequest(BaseModel):
    question:str

@app.post("/ask")
def ask_question(req: QueryRequest):
    if not is_safe_query(req.question):
        raise HTTPException(status_code=400, detail="Unsafe query.")
    response=agent.run(req.question)
    return {"answer": response}
