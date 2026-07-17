from typing import TypedDict


class State(TypedDict, total=False):

    # ----------------------------
    # Discovery
    # ----------------------------

    company: str
    url: str
    filtered_links: list[dict]
    important_pages: list[dict]

    # ----------------------------
    # Intelligence
    # ----------------------------

    category: str
    content: str
    added: list[str]
    removed: list[str]

    analysis: dict