import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from tools import calculator


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