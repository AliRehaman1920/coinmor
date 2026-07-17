import json
from pathlib import Path

from langchain_core.messages import SystemMessage, HumanMessage

from llm import llm
from graph.state import State


def discovery_node(state: State):

    discovery_prompt = Path("graph/prompts/discovery_node.md").read_text(
        encoding="utf-8"
    )

    messages = [
        SystemMessage(content=discovery_prompt),
        HumanMessage(
            content=f"""
Homepage:
{state["url"]}

Filtered Links:
{state["filtered_links"]}
"""
        ),
    ]

    response = llm.invoke(messages)

    try:
        important_pages = json.loads(response.content)

    except json.JSONDecodeError as e:

        print("\nLLM Response:")
        print(response.content)

        raise e

    return {
        "important_pages": important_pages
    }