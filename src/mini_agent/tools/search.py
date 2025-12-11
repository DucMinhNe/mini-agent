"""Web search tool."""
from __future__ import annotations
from typing import Any


class SearchTool:
    """Web search tool."""

    def __init__(self, **config: Any) -> None:
        self.config = config

    def name(self, *args, **kwargs):
        """Return 'search'."""
        raise NotImplementedError

    def run(self, *args, **kwargs):
        """Run DuckDuckGo search."""
        raise NotImplementedError
