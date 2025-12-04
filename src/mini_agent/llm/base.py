"""Abstract LLM client."""
from __future__ import annotations
from typing import Any


class LLMClient:
    """Abstract LLM client."""

    def __init__(self, **config: Any) -> None:
        self.config = config

    def complete(self, *args, **kwargs):
        """Complete a prompt."""
        raise NotImplementedError

    def stream(self, *args, **kwargs):
        """Stream completion tokens."""
        raise NotImplementedError
