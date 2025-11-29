"""OpenAI client."""
from __future__ import annotations
from typing import Any


class OpenAIClient:
    """OpenAI client."""

    def __init__(self, **config: Any) -> None:
        self.config = config

    def complete(self, *args, **kwargs):
        """Call OpenAI chat completions."""
        raise NotImplementedError

    def stream(self, *args, **kwargs):
        """Stream OpenAI tokens."""
        raise NotImplementedError
