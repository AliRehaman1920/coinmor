import asyncio
import json
import os

from discovery.discover import run_discovery
from monitoring import monitor_company


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

                    # get links that are worth tracking filtered by filer_links() and discovey node
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

            
            tasks = []

            for file in monitoring_files:

                with open(file, "r", encoding="utf-8") as f:
                    monitoring_plan = json.load(f)

                company = monitoring_plan["company"]
                url = monitoring_plan["url"]

                tasks.append(
                    monitor_company(company, url)
                )

            await asyncio.gather(*tasks)

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