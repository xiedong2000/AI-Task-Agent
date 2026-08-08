import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from tools import calculator,read_document

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform a mathematical calculation.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A mathematical expression to calculate."
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_document",
            "description": "Read the content of a document.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "The name of the document to read."
                    }
                },
                "required": ["filename"]
            }
        }
    }
]


def run_agent(user_question):
    messages = [
        {
            "role": "user",
            "content": user_question
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if message.tool_calls:
        messages.append(message)

        for tool_call in message.tool_calls:
            if tool_call.function.name == "calculator":
                arguments = json.loads(tool_call.function.arguments)

                expression = arguments["expression"]

                print(f"\nTool selected: calculator")
                print(f"Expression: {expression}")

                result = calculator(expression)

                print(f"Tool result: {result}")

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result
                    }
                )

            elif tool_call.function.name == "read_document":
                arguments = json.loads(tool_call.function.arguments)

                filename = arguments["filename"]

                print(f"\nTool selected: read_document")
                print(f"Filename: {filename}")

                result = read_document(filename)

                print(f"Tool result: \n{result}")

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result
                    }
                )

        final_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        return final_response.choices[0].message.content

    return message.content


if __name__ == "__main__":
    question = input("Ask the AI agent: ")

    answer = run_agent(question)

    print("\nAI Agent:")
    print(answer)