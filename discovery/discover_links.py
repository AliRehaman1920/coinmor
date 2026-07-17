
from urllib.parse import urljoin

from playwright.async_api import Page


"""
discover_links.py

Extract all links from a single webpage.

Responsibilities:
- Open the webpage
- Extract every <a href=""> element
- Convert relative URLs to absolute URLs
- Return the URL and anchor text

Filtering and ranking happen later in preprocess_links().
"""


async def discover_links(url: str, page: Page) -> list[dict]:
    """
    Extract every link from a webpage.

    Args:
        url: Homepage URL.
        page: Playwright page.

    Returns:
        List of dictionaries:
        [
            {
                "url": "...",
                "anchor_text": "..."
            }
        ]
    """

    await page.goto(url, wait_until="domcontentloaded")

    anchors = await page.query_selector_all("a[href]")

    links = []

    for anchor in anchors:

        href = await anchor.get_attribute("href")

        if href is None:
            continue

        absolute_url = urljoin(url, href)

        anchor_text = (await anchor.inner_text()).strip()

        links.append(
            {
                "url": absolute_url,
                "anchor_text": anchor_text
            }
        )

    return links
