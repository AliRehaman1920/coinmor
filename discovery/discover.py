import json

from playwright.async_api import async_playwright

from discovery.discover_links import discover_links
from discovery.filter import filter_links
from graph.discovery_graph import discovery_graph


async def run_discovery(company: str, url: str):

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)

        page = await browser.new_page()

        raw_links = await discover_links(url, page)

        print(f"Found {len(raw_links)} links")

        filtered_links = filter_links(raw_links, url)

        print(f"Filtered {len(filtered_links)} links")

        await browser.close()

    state = {
        "company": company,
        "url": url,
        "filtered_links": filtered_links
    }

    result = discovery_graph.invoke(state)

    with open(f"company_links/{company.lower()}.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)

    return result