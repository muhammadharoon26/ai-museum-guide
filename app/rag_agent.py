from langchain.agents import initialize_agent, Tool
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from app.vectorstore import get_vectorstore
from app.wiki_tool import search_wikipedia
from app.cache import memory


def get_agent():
    retriever = get_vectorstore().as_retriever()

    # Initialize model and tokenizer
    model_id = "google/flan-t5-base"  # Using smaller base model that can run locally
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
    
    # Create pipeline
    pipe = pipeline(
        "text2text-generation",
        model=model, 
        tokenizer=tokenizer,
        max_length=512,
        temperature=0.3,
    )
    
    # Create LangChain LLM
    llm = HuggingFacePipeline(pipeline=pipe)

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    tools = [
        Tool(name="MuseumRetriever", func=qa_chain.run, description="Get museum info"),
        Tool(name="Wikipedia", func=search_wikipedia, description="Get general knowledge"),
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True,
        memory=memory,
    )

    return agent