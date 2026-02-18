"""Safe arithmetic evaluator."""
from __future__ import annotations
from typing import Any


class CalculatorTool:
    """Safe arithmetic evaluator."""

    def __init__(self, **config: Any) -> None:
        self.config = config

    def name(self, *args, **kwargs):
        """Return 'calc'."""
        raise NotImplementedError

    def run(self, *args, **kwargs):
        """Eval expression."""
        raise NotImplementedError
