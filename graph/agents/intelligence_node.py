import json
from pathlib import Path

from langchain_core.messages import SystemMessage, HumanMessage

from llm import llm
from graph.state import State


def intelligence_node(state: State):

    intelligence_prompt = Path("graph/prompts/intelligence_node.md").read_text(
        encoding="utf-8"
    )

    messages = [
        SystemMessage(content=intelligence_prompt),
        HumanMessage(
            content=f"""
Company:
{state["company"]}

Category:
{state["category"]}

URL:
{state["url"]}

Added Content:
{state["added"]}

Removed Content:
{state["removed"]}
"""
        ),
    ]

    response = llm.invoke(messages)

    try:
        content = response.content.strip()

        if content.startswith("```json"):
            content = content.removeprefix("```json").strip()

        if content.endswith("```"):
            content = content.removesuffix("```").strip()

        analysis = json.loads(content)

    except json.JSONDecodeError as e:
        print("\nLLM Response:")
        print(response.content)
        return {"analysis": {"summary": "Could not analyze this page (invalid AI response)."}}

    return {
        "analysis": analysis
    }