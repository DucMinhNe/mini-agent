# 🤖 mini-agent

> A lightweight, modular AI agent framework with pluggable tools, multi-LLM support, and a FastAPI server.

[![CI](https://github.com/DucMinhNe/mini-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/DucMinhNe/mini-agent/actions/workflows/ci.yml) ![license](https://img.shields.io/badge/license-MIT-green.svg) ![python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg) ![code style](https://img.shields.io/badge/code%20style-black-000000.svg) ![PRs](https://img.shields.io/badge/PRs-welcome-orange.svg)

---

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Quick start](#quick-start)
- [Usage](#usage)
- [Configuration](#configuration)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- 🧠 Multi-LLM backends: OpenAI, Google Gemini
- 🔧 Pluggable tool system (search, calculator, file reader, code exec)
- 💾 Conversation memory with configurable window
- ⚡ FastAPI server with streaming endpoints
- 🐚 Typer-based CLI
- 🐳 Dockerfile + docker-compose
- ✅ Type hints throughout
- 📚 Examples & docs

## Architecture

```
user ──▶ Agent ──▶ LLMClient ──▶ {OpenAI, Gemini}
             │
             └──▶ ToolRegistry ──▶ {search, calc, file, code_exec}
```

## Installation

**Using pip:**

```bash
pip install -e .
```

**Using Docker:**

```bash
docker build -t mini-agent . && docker run --rm -e OPENAI_API_KEY=$OPENAI_API_KEY mini-agent
```

## Quick start

```python
from mini_agent import Agent

agent = Agent(model="gpt-4o-mini")
print(agent.run("What is the capital of Vietnam?"))
```

## Usage

### Basic chat

```python
from mini_agent import Agent
agent = Agent()
print(agent.run("hi"))
```

### With tools

```python
from mini_agent import Agent
from mini_agent.tools import SearchTool, CalculatorTool
agent = Agent(tools=[SearchTool(), CalculatorTool()])
print(agent.run("13.4 * 8 then search wikipedia for the result"))
```

### Run as API

```python
uvicorn mini_agent.server.app:app --reload
```

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | - | OpenAI API key |
| `GEMINI_API_KEY` | - | Gemini API key |
| `MINI_AGENT_MODEL` | gpt-4o-mini | Default LLM model |
| `MINI_AGENT_MAX_STEPS` | 10 | Max tool-use iterations |

## Roadmap

- [x] Core agent loop
- [x] OpenAI + Gemini backends
- [x] Search, calculator, file tools
- [x] CLI
- [x] FastAPI server
- [ ] Multi-agent orchestration
- [ ] Streaming tokens over websocket
- [ ] Plugin marketplace

## Contributing

PRs welcome. Please open an issue first to discuss any non-trivial change.
Run `ruff check .` and `pytest` before submitting.

## License

MIT — see [LICENSE](./LICENSE).

---

_Made with care in Hanoi._ 🌱
