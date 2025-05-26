from langchain.agents import initialize_agent, Tool
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
from app.vectorstore import get_vectorstore
from app.wiki_tool import search_wikipedia
from app.cache import memory


def get_agent():
    retriever = get_vectorstore().as_retriever()

    llm = HuggingFaceHub(
        repo_id="google/flan-t5-xl",
        model_kwargs={"temperature": 0.3, "max_length": 512},
    )

    qa_chain=RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    tools=[
        Tool(name="MuseumRetriever", func=qa_chain.run, description="Get museum info"),
        Tool(name="Wikipedia", func=search_wikipedia, description="Get general knowledge"),
    ]

    agent=initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True,
        memory=memory,
    )

    return agent