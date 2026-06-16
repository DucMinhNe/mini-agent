"""Tool registry."""


from .base import Tool
from .calculator import CalculatorTool
from .file_reader import FileReaderTool
from .search import SearchTool

__all__ = ["Tool", "CalculatorTool", "FileReaderTool", "SearchTool", "register"]

_registry = {}


def register(tool):
    _registry[tool.name()] = tool
