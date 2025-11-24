class MemoryEngine:
    """
    Basic short-term memory engine for Agentra.uk (v0.2).

    This will evolve into a more advanced context and long-term
    memory system in future versions (v0.3+).
    """

    def __init__(self):
        # Simple in-memory list for now
        self._buffer = []

    def add(self, item: str) -> None:
        """
        Store a new memory item (e.g. tool output, reasoning step).
        """
        self._buffer.append(item)

    def recall_all(self):
        """
        Return all stored memory items.
        """
        return list(self._buffer)

    def clear(self) -> None:
        """
        Clear the memory buffer.
        """
        self._buffer.clear()
