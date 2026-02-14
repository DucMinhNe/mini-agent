"""Multiple agents coordinating."""
from __future__ import annotations
from typing import Any


class AgentSwarm:
    """Multiple agents coordinating."""

    def __init__(self, **config: Any) -> None:
        self.config = config

    def dispatch(self, *args, **kwargs):
        """Round-robin dispatch."""
        raise NotImplementedError

    def aggregate(self, *args, **kwargs):
        """Aggregate responses."""
        raise NotImplementedError
