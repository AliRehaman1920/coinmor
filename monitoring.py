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