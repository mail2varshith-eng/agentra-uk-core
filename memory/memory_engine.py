class MemoryEngine:
    """
    Basic short-term memory engine for Agentra.uk (v0.2).

    This will evolve into a more advanced context and long-term
    memory system in future versions (v0.3+).
    """

    def __init__(self) -> None:
        # Simple in-memory buffer for now
        self._buffer = []

    def add(self, item: str) -> None:
        """
        Store a new memory item.

        Example items:
        - intermediate reasoning steps
        - tool outputs
        - user context notes
        """
        self._buffer.append(item)

    def recall_all(self):
        """
        Return all stored memory items as a list.
        """
        return list(self._buffer)

    def last(self):
        """
        Return the most recent memory item, or None if empty.
        """
        if not self._buffer:
            return None
        return self._buffer[-1]

    def clear(self) -> None:
        """
        Clear the memory buffer.
        """
        self._buffer.clear()
