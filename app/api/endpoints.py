from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.qa_service import get_qa_chain
from app.guardrails import is_safe_query

router = APIRouter()
qa_chain = get_qa_chain()

class QueryRequest(BaseModel):
    question: str

@router.post("/ask")
def ask_question(req: QueryRequest):
    if not is_safe_query(req.question):
        raise HTTPException(status_code=400, detail="Unsafe query.")
    response = qa_chain.invoke({"query": req.question})
    return {"answer": response["result"]}
