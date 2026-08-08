# AI Task Agent

An AI agent application built with Python and the OpenAI API to explore **LLM tool calling, agent workflows, multi-step task execution, and AI application evaluation**.

The project is being developed as part of my hands-on transition into AI application engineering.

## Project Status

🚧 **In Development**

The current version demonstrates a basic AI agent that can decide when to use a calculator tool and return the result through the OpenAI model.

Future versions will add document processing, multiple tools, multi-step workflows, RAG integration, evaluation, and production deployment.

---

## What I Am Learning

This project focuses on the following AI engineering concepts:

- OpenAI API
- LLM tool/function calling
- AI agent architecture
- Tool selection
- Structured tool arguments
- Multi-step workflows
- Agent state and context
- Error handling
- AI evaluation
- RAG integration
- AI application architecture
- FastAPI and deployment

The goal is to understand the underlying agent workflow before introducing agent frameworks such as LangChain or LangGraph.

---

## Current Agent Architecture

The initial agent uses a simple tool-calling loop:

```text
                    User Request
                         │
                         ▼
                  ┌─────────────┐
                  │     LLM     │
                  └──────┬──────┘
                         │
                  Tool required?
                    ┌────┴────┐
                   Yes        No
                    │          │
                    ▼          ▼
              Execute Tool   Answer
                    │
                    ▼
                Tool Result
                    │
                    ▼
                   LLM
                    │
                    ▼
               Final Answer
```

The important concept is that the LLM does not directly execute Python functions.

Instead:

1. The application describes available tools to the LLM.
2. The LLM determines whether a tool is needed.
3. The LLM generates the tool arguments.
4. Python executes the selected tool.
5. The tool result is returned to the LLM.
6. The LLM generates the final response.

---

## Current Tool

### Calculator

The first version includes a calculator tool.

Example:

```text
Ask the AI agent: What is 125 * 18%?

Tool selected: calculator
Expression: 125 * 18%
Tool result: 22.5

AI Agent:
125 * 18% = 22.5
```

The agent should also recognize when a tool is not necessary.

For example:

```text
Ask the AI agent: What is artificial intelligence?

AI Agent:
Artificial intelligence is...
```

In this case, the calculator tool is not used.

---

## Project Structure

```text
AI-Task-Agent/
│
├── code/
│   ├── agent.py
│   └── tools.py
│
├── docs/
│   └── sample.txt
│
├── tests/
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

### Key Files

**`code/agent.py`**

Contains the main agent loop, OpenAI client configuration, tool definitions, tool selection, and response generation.

**`code/tools.py`**

Contains the Python implementations of tools available to the agent.

**`requirements.txt`**

Contains the Python dependencies required by the project.

**`.env`**

Contains the local OpenAI API key. This file must never be committed to GitHub.

---

# Development Environment

This project uses **Python 3.12**.

Multiple Python versions may be installed on the development machine, so the virtual environment should be created explicitly with Python 3.12.

## Create Virtual Environment

From PowerShell:

```powershell
cd C:\Development\Dong_AI\AI-Task-Agent

py -3.12 -m venv ai-env
```

## Activate Virtual Environment

```powershell
ai-env\Scripts\activate
```

The PowerShell prompt should show:

```text
(ai-env) PS C:\Development\Dong_AI\AI-Task-Agent>
```

## Verify Python Version

```powershell
python --version
```

Expected:

```text
Python 3.12.x
```

You can also verify which Python executable is being used:

```powershell
where.exe python
```

The first result should be:

```text
C:\Development\Dong_AI\AI-Task-Agent\ai-env\Scripts\python.exe
```

### Why Python 3.12?

The development machine has multiple Python installations. Using:

```powershell
py -3.12 -m venv ai-env
```

ensures that the virtual environment is created with Python 3.12 instead of another installed version.

---

# Install Dependencies

After activating the virtual environment, upgrade `pip`:

```powershell
python -m pip install --upgrade pip
```

Then install the project dependencies:

```powershell
pip install -r requirements.txt
```

The current dependencies include:

- `openai` — OpenAI Python SDK
- `python-dotenv` — loads environment variables from `.env`

## Verify Installation

Verify the OpenAI package:

```powershell
python -c "import openai; print(openai.__version__)"
```

Verify `python-dotenv`:

```powershell
python -c "from dotenv import load_dotenv; print('python-dotenv OK')"
```

---

# OpenAI API Configuration

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
```

The application loads the API key using `python-dotenv`.

Do **not** hard-code the API key in Python source code.

Do **not** commit `.env` to GitHub.

The `.gitignore` file excludes `.env` from source control.

---

# Run the Agent

Make sure the virtual environment is active:

```powershell
ai-env\Scripts\activate
```

Then run:

```powershell
python code/agent.py
```

The application will prompt:

```text
Ask the AI agent:
```

Example:

```text
Ask the AI agent: What is 125 * 18%?
```

The agent should determine that the calculator tool is appropriate, execute the tool, and return the result.

---

# Learning Progression

The project is being developed incrementally.

### Phase 1 — Basic Tool Calling

- [x] Python 3.12 virtual environment
- [x] OpenAI Python SDK
- [x] Environment variable configuration
- [x] Basic OpenAI API call
- [x] Calculator tool
- [x] Tool selection
- [x] Tool execution
- [x] Return tool result to LLM
- [x] Generate final answer

### Phase 2 — Multiple Tools

- [ ] Document reader
- [ ] Current date/time tool
- [ ] Multiple tool definitions
- [ ] Tool error handling
- [ ] Tool execution logging

### Phase 3 — Multi-Step Agent

- [ ] Multi-tool tasks
- [ ] Agent loop
- [ ] Maintain conversation state
- [ ] Structured outputs
- [ ] More robust tool validation
- [ ] Handle failed tool calls

### Phase 4 — RAG Integration

Integrate concepts from my existing PDF RAG project.

- [ ] RAG search as an agent tool
- [ ] Retrieve relevant document chunks
- [ ] Agent decides when RAG is needed
- [ ] Combine RAG with other tools
- [ ] Evaluate retrieval and answer quality

Project:

[PDF-RAG-Assistant](https://github.com/xiedong2000/PDF-RAG-Assistant)

### Phase 5 — Agent Evaluation

Create a test set to evaluate:

- Tool selection accuracy
- Tool argument accuracy
- Final answer accuracy
- Retrieval quality
- Failure handling
- Response latency
- API cost

Example:

```text
Test Case
    ↓
Agent
    ↓
Expected Tool
    ↓
Actual Tool
    ↓
Expected Answer
    ↓
Actual Answer
    ↓
Evaluation
```

### Phase 6 — Production AI

Explore production-oriented AI application development:

- [ ] FastAPI
- [ ] REST API
- [ ] Authentication
- [ ] Database persistence
- [ ] Docker
- [ ] Logging
- [ ] Error monitoring
- [ ] API rate limiting
- [ ] Cloud deployment

---

# Relationship to My Other AI Projects

This project is part of a broader hands-on AI engineering portfolio.

## PDF-RAG-Assistant

A Retrieval-Augmented Generation application that answers questions about PDF documents.

Key technologies:

- Python
- OpenAI
- Embeddings
- ChromaDB
- PyPDF
- Streamlit
- RAG

Repository:

[PDF-RAG-Assistant](https://github.com/xiedong2000/PDF-RAG-Assistant)

## ShortsAI Studio

A multimodal AI application that transforms short videos into YouTube Shorts.

The application explores:

- Video processing
- Speech-to-text
- LLM-generated content
- On-screen captions
- Titles and descriptions
- Tags
- Music
- Automated video generation
- Streamlit UI

Repository:

[ShortsAI-Studio](https://github.com/xiedong2000/ShortsAI-Studio)

## AI Task Agent

This project focuses on:

- Tool calling
- AI agents
- Multi-step workflows
- Agent evaluation
- RAG as an agent capability
- Production AI architecture

Together, these projects provide hands-on experience across several areas of AI application engineering.

---

# Development Notes

A key lesson from setting up this project was the importance of explicitly controlling the Python version used to create a virtual environment.

The development machine contains multiple Python versions. Creating the environment with:

```powershell
python -m venv ai-env
```

can select an unintended Python installation.

Using:

```powershell
py -3.12 -m venv ai-env
```

makes the Python version explicit and avoids compatibility problems.

Another important lesson is to keep the virtual environment and secrets outside Git source control.

---

# Future Direction

The long-term goal is to evolve this project from a simple tool-calling demonstration into a production-oriented AI agent.

The planned architecture is:

```text
                         User
                           │
                           ▼
                     AI Task Agent
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
        Calculator       RAG         Documents
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                     Tool Results
                           │
                           ▼
                          LLM
                           │
                           ▼
                     Final Response
```

The project will emphasize understanding the underlying AI engineering concepts rather than relying on an agent framework immediately.

---

# License

This project is intended for educational and portfolio purposes.