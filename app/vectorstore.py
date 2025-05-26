import json
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document

def load_data(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return [Document(page_content=item['description'], metadata={'title': item['title']}) for item in data]

def get_vectorstore():
    docs = load_data('app/data/musuem_data.json')
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
