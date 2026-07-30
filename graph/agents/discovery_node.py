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
        return {"important_pages": []}   # same fallback idea as before — don't crash

    # NEW: only keep pages whose URL was actually in filtered_links
    valid_urls = {link["url"] for link in state["filtered_links"]}
    important_pages = [
        page for page in important_pages
        if page.get("url") in valid_urls
    ]

    return {"important_pages": important_pages}