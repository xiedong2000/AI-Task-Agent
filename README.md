# AI Task Agent

An AI agent application that uses an OpenAI model and tool calling to perform tasks through multiple tools and multi-step workflows.

## Project Status

🚧 **In Development**

The first version focuses on learning the fundamentals of AI agents and function/tool calling by implementing the agent loop directly with the OpenAI API.

## Development Environment

This project uses **Python 3.12**.

### Create the Virtual Environment

From PowerShell:

```powershell
cd C:\Development\Dong_AI\AI-Task-Agent

py -3.12 -m venv ai-env
```

Activate the virtual environment:

```powershell
ai-env\Scripts\activate
```

Verify the Python version:

```powershell
python --version
```

The expected result is:

```text
Python 3.12.x
```

### Why Python 3.12?

The virtual environment must be created explicitly with Python 3.12 because multiple Python versions may be installed on the development machine.

Using:

```powershell
py -3.12 -m venv ai-env
```

ensures that the virtual environment uses Python 3.12 rather than another installed version.

### Install Dependencies

After activating the virtual environment:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
```

Do not commit `.env` or API keys to source control.

## Planned Agent Architecture

The initial agent will use a simple tool-calling loop:

```text
User Request
     ↓
   OpenAI
     ↓
Tool Required?
   ↙       ↘
 Yes        No
  ↓          ↓
Execute     Answer
Tool
  ↓
Tool Result
  ↓
OpenAI
  ↓
Final Answer
```

## Initial Tools

The first version will include:

- Calculator
- Document reader
- Current date/time

The project will later explore multi-tool workflows, structured outputs, error handling, evaluation, and integration with the PDF RAG project.