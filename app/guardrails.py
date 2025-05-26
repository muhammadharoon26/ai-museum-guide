def is_safe_query(query: str) -> bool:
    banned_keywords = ["kill", "suicide", "violence", "terrorist"]
    return not any(word in query.lower() for word in banned_keywords)
