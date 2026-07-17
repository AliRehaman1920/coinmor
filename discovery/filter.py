# filter.py

from urllib.parse import urlparse, urlunparse


def filter_links(links: list[dict], homepage_url: str) -> list[dict]:

    # Get the company's main domain
    homepage_domain = urlparse(homepage_url).netloc

    filtered_links = []
    seen = set()

    # Keywords for pages we never want to monitor
    ignored_keywords = [
        "privacy",
        "legal",
        "terms",
        "cookie",
        "account",
        "login",
        "signup",
    ]

    for link in links:

        url = link["url"]
        anchor_text = link["anchor_text"]

        # Skip invalid URLs
        if (
            url.startswith("javascript:")
            or url.startswith("mailto:")
            or url.startswith("tel:")
            or url.startswith("#")
        ):
            continue

        # Skip external websites
        link_domain = urlparse(url).netloc

        if homepage_domain not in link_domain:
            continue

        # Remove tracking parameters and fragments
        parsed = urlparse(url)

        clean_url = urlunparse(
            parsed._replace(query="", fragment="")
        ).rstrip("/")

        # Skip duplicate URLs
        if clean_url in seen:
            continue

        seen.add(clean_url)

        # Skip boilerplate pages
        lower_url = clean_url.lower()

        if any(keyword in lower_url for keyword in ignored_keywords):
            continue

        filtered_links.append(
            {
                "url": clean_url,
                "anchor_text": anchor_text,
            }
        )

    return filtered_links