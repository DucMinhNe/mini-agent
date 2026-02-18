"""Sliding-window conversation memory."""
from __future__ import annotations
from typing import Any


class Memory:
    """Sliding-window conversation memory."""

    def __init__(self, **config: Any) -> None:
        self.config = config

    def add(self, *args, **kwargs):
        """Append a message."""
        raise NotImplementedError

    def snapshot(self, *args, **kwargs):
        """Return current window."""
        raise NotImplementedError
