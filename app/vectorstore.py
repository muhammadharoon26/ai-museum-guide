import json
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

def load_data(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return [Document(page_content=entry['description'], metadata={'title': entry['title']}) for item in data]

def get_vectorstore():
    docs = load_data('app/data/musuem_data.json')
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/instructor-xl')
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
