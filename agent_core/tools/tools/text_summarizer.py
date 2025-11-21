def simple_summarise(text: str, max_sentences: int = 3) -> str:
    """
    Extremely basic 'summariser':
    - Split by newline
    - Return first N lines
    This is intentionally simple for MVP evidence.
    """

    lines = [line.strip() for line in text.split("\n") if line.strip()]
    selected = lines[:max_sentences]
    return "SUMMARY:\n" + "\n".join(selected)
