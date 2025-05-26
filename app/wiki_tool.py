from langchain.tools import tool
import wikipedia

@tool
def search_wikipedia(query: str) -> str:
    """Search Wikipedia for additionalinformation."""
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception as e:
        return f"No results found.Error: {e}"

