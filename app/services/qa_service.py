from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from app.data_layer.vectorstore import get_vectorstore


def get_qa_chain():
    retriever = get_vectorstore().as_retriever()
    model_id = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
    pipe = pipeline(
        "text2text-generation",
        model=model, 
        tokenizer=tokenizer,
        max_length=512,
    )
    llm = HuggingFacePipeline(pipeline=pipe)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain 