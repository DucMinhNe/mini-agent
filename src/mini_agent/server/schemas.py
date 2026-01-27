"""Data model for ChatRequest."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class ChatRequest:
    message: str
    model: str
    stream: bool
