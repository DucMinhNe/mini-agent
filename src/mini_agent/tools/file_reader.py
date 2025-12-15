"""Read files from sandbox."""
from __future__ import annotations
from typing import Any


class FileReaderTool:
    """Read files from sandbox."""

    def __init__(self, **config: Any) -> None:
        self.config = config

    def name(self, *args, **kwargs):
        """Return 'file'."""
        raise NotImplementedError

    def run(self, *args, **kwargs):
        """Read a file path."""
        raise NotImplementedError
