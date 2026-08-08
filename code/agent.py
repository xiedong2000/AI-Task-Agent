import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from tools import calculator,read_document, get_current_datetime

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
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_datetime",
            "description": (
                "Get the current local date and time. "
                "Use this tool when the user asks for the current "
                "date or time."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
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

    max_iterations = 10
    iteration = 0

    while iteration < max_iterations:
        iteration += 1

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        message = response.choices[0].message

        

        # No tool needed - return the final answer
        if not message.tool_calls:
            return message.content

        # Add the assistant's tool request to the conversation
        messages.append(message)

        # print("\nDEBUG")
        # print("Content:", message.content)
        # print("Tool calls:", message.tool_calls)

        # Execute every tool requested by the model
        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            if tool_call.function.name == "calculator":
                expression = arguments["expression"]

                print(f"\nTool selected: calculator")
                print(f"Expression: {expression}")

                result = calculator(expression)

            elif tool_call.function.name == "read_document":
                filename = arguments["filename"]

                print(f"\nTool selected: read_document")
                print(f"Filename: {filename}")

                result = read_document(filename)

                print(f"Tool result: \n{result}")

            elif tool_call.function.name == "get_current_datetime":
                print(f"\nTool selected: get_current_datetime")

                result = get_current_datetime()

                print(f"Tool result: \n{result}")

            # Send the tool result back to the model
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