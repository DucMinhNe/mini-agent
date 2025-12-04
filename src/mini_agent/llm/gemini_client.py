"""Google Gemini client."""
from __future__ import annotations
from typing import Any


class GeminiClient:
    """Google Gemini client."""

    def __init__(self, **config: Any) -> None:
        self.config = config

    def complete(self, *args, **kwargs):
        """Call Gemini generate_content."""
        raise NotImplementedError

    def stream(self, *args, **kwargs):
        """Stream Gemini tokens."""
        raise NotImplementedError
