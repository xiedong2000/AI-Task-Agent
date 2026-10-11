import sys
from pathlib import Path

# Add the project root to Python's module search path.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.agent import run_agent, tools
from src.tools import read_document


def test_search_tool_is_registered():
    tool_names = {tool["function"]["name"] for tool in tools}
    assert "search_documents" in tool_names


def test_read_document_supports_pdf(tmp_path):
    pdf_path = tmp_path / "sample.pdf"
    pdf_bytes = (
        b"""%PDF-1.4
1 0 obj
<< /Type /Catalog /Pages 2 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [3 0 R] /Count 1 >>
endobj
3 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 300 200] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>
endobj
4 0 obj
<< /Length 55 >>
stream
BT
/F1 24 Tf
50 100 Td
(Hello from PDF) Tj
ET
endstream
endobj
5 0 obj
<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>
endobj
xref
0 6
0000000000 65535 f 
0000000010 00000 n 
0000000062 00000 n 
0000000123 00000 n 
0000000245 00000 n 
0000000648 00000 n 
trailer
<< /Root 1 0 R /Size 6 >>
startxref
742
%%EOF
""" + b"\x00\xe2\x00\xff"
    )
    pdf_path.write_bytes(pdf_bytes)

    content = read_document(str(pdf_path))

    assert "Hello from PDF" in content
    assert "Document error" not in content


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