import asyncio
import json
import os

from discovery.discover import run_discovery
from collection.collect import run_collection
from snapshot.snapshots import process_snapshots
from graph.intelligence_graph import intelligence_graph
from reports.write_to_file import write_analysis


async def monitor_company(company: str, url: str):

    print(f"\nMonitoring {company}...\n")

    collected_pages = await run_collection(company)

    if not collected_pages:
        print(f"No pages collected for {company}.")
        return

    changed_pages = process_snapshots(company, collected_pages)

    if not changed_pages:
        print(f"No changes detected for {company}.")
        return

    print(f"{len(changed_pages)} page(s) changed.\n")

    for page in changed_pages:

        result = await intelligence_graph.ainvoke(page)

        analysis = result["analysis"]

        write_analysis(
            company=company,
            category=page["category"],
            url=page["url"],
            summary=analysis["summary"],
        )

    print(f"Finished monitoring {company}.\n")


async def main():

    while True:

        print("\n=== Competitive Intelligence Monitor ===")
        print("1. Add company")
        print("2. Monitor existing companies")
        print("3. Exit")

        choice = input("\nSelect an option: ").strip()

        # --------------------------------------------------
        # Add company
        # --------------------------------------------------

        if choice == "1":

            while True:

                company = input("\nCompany name: ").strip()
                url = input("Homepage URL: ").strip()

                monitoring_plan = f"{company.lower()}.json"

                if os.path.exists(monitoring_plan):
                    print(f"{company} is already being monitored.")
                else:
                    print(f"Adding {company}...")
                    await run_discovery(company, url)
                    print(f"{company} added successfully.")

                another = input("\nAdd another company? (y/n): ").strip().lower()

                if another != "y":
                    break

        # --------------------------------------------------
        # Monitor companies
        # --------------------------------------------------

        elif choice == "2":

            monitoring_files = [
                file for file in os.listdir(".")
                if file.endswith(".json")
            ]

            if not monitoring_files:
                print("\nNo companies to monitor. Add at least one company.")
                continue

            for file in monitoring_files:

                with open(file, "r", encoding="utf-8") as f:
                    monitoring_plan = json.load(f)

                company = monitoring_plan["company"]
                url = monitoring_plan["homepage"]

                await monitor_company(company, url)

        # --------------------------------------------------
        # Exit
        # --------------------------------------------------

        elif choice == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    asyncio.run(main())