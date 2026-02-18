"""Base tool."""
from __future__ import annotations
from typing import Any


class Tool:
    """Base tool."""

    def __init__(self, **config: Any) -> None:
        self.config = config

    def name(self, *args, **kwargs):
        """Tool name."""
        raise NotImplementedError

    def run(self, *args, **kwargs):
        """Execute the tool."""
        raise NotImplementedError
