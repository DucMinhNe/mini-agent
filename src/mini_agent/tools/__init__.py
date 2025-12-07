"""Tool registry."""


from .base import Tool

_registry = {}


def register(tool):
    _registry[tool.name()] = tool
