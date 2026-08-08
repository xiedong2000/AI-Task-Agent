import sys
from pathlib import Path

# Add the project root to Python's module search path.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.agent import run_agent


test_cases = [
    {
        "question": "What is 25 * 4?",
        "expected_tools": ["calculator"],
    },
    {
        "question": "What does docs/sample.txt say about RAG?",
        "expected_tools": ["read_document"],
    },
    {
        "question": "What is the current date and time?",
        "expected_tools": ["get_current_datetime"],
    },
    {
        "question": "What is artificial intelligence?",
        "expected_tools": [],
    },
    {
        "question": (
            "Read docs/sample.txt and calculate the average "
            "of the three project numbers."
        ),
        "expected_tools": ["read_document", "calculator"],
    },
]


passed = 0


for test in test_cases:
    print("\n" + "=" * 60)
    print(f"Question: {test['question']}")
    print(f"Expected tools: {test['expected_tools']}")

    result = run_agent(test["question"])

    actual_tools = result["tools_used"]

    if test["expected_tools"] is None:
        success = len(actual_tools) == 0
    else:
        success = all(
            tool in actual_tools
            for tool in test["expected_tools"]
        )

    if success:
        print("PASS")
        passed += 1
    else:
        print("FAIL")
        print(f"Expected: {test['expected_tools']}")
        print(f"Actual: {actual_tools}")

    print(f"Answer: {result['answer']}")


print("\n" + "=" * 60)
print(f"Tests passed: {passed}/{len(test_cases)}")
print(f"Accuracy: {passed / len(test_cases) * 100:.1f}%")