import os
import difflib


def process_snapshots(company: str, collected_pages: list):
    """
    Processes all collected pages.

    Responsibilities:
    - Create snapshot folder if needed.
    - Create snapshot files on first run.
    - Compare current content with previous snapshot.
    - Update snapshots when changes occur.
    - Return only the pages that changed.
    """

    company_folder = os.path.join("snapshots", company.lower())

    os.makedirs(company_folder, exist_ok=True)

    changed_pages = []

    for page in collected_pages:

        url = page["url"]
        category = page["category"]
        content = page["content"]

        # --------------------------------------------
        # Create filename from URL
        # --------------------------------------------

        filename = url.rstrip("/").split("/")[-1]

        if filename == "":
            filename = "homepage"

        snapshot_file = os.path.join(
            company_folder,
            f"{category.lower()}_{filename}.txt"
        )

        print("=" * 80)
        print(f"Checking: {snapshot_file}")

        # --------------------------------------------
        # First run
        # --------------------------------------------

        if not os.path.exists(snapshot_file):

            with open(snapshot_file, "w", encoding="utf-8") as file:
                file.write(content)

            print("Snapshot created.\n")

            changed_pages.append({
                "company": company,
                "url": url,
                "category": category,
                "content": content,
                "added": content.splitlines(),
                "removed": [],
                "is_first_snapshot": True,
            })

            continue

        # --------------------------------------------
        # Read previous snapshot
        # --------------------------------------------

        with open(snapshot_file, "r", encoding="utf-8") as file:
            old_content = file.read()

        # --------------------------------------------
        # No changes
        # --------------------------------------------

        if old_content == content:

            print("No changes detected.\n")
            continue

        print("Changes detected.")

        # --------------------------------------------
        # Compute diff
        # --------------------------------------------

        diff = difflib.unified_diff(
            old_content.splitlines(),
            content.splitlines(),
            lineterm=""
        )

        added = []
        removed = []

        for line in diff:

            if line.startswith(("---", "+++", "@@")):
                continue

            if line.startswith("+"):
                added.append(line[1:])

            elif line.startswith("-"):
                removed.append(line[1:])

        # --------------------------------------------
        # Update snapshot
        # --------------------------------------------

        with open(snapshot_file, "w", encoding="utf-8") as file:
            file.write(content)

        print("Snapshot updated.\n")

        # --------------------------------------------
        # Save changed page
        # --------------------------------------------

        changed_pages.append({

            "company": company,
            "url": url,
            "category": category,
            "content": content,
            "added": added,
            "removed": removed,
            "is_first_snapshot": False,

        })

    return changed_pages