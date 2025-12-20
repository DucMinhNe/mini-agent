"""Tool-using agent."""
from __future__ import annotations
from typing import Any


class Agent:
    """Tool-using agent."""

    def __init__(self, **config: Any) -> None:
        self.config = config

    def run(self, *args, **kwargs):
        """Run a single turn."""
        raise NotImplementedError

    def step(self, *args, **kwargs):
        """One agent step."""
        raise NotImplementedError

    def _select_tool(self, *args, **kwargs):
        """Pick a tool for this step."""
        raise NotImplementedError
