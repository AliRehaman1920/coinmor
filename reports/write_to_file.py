from pathlib import Path


def write_analysis(
    company: str,
    category: str,
    url: str,
    summary: str,
) -> None:
    """
    Appends one page analysis to the company's report.
    Creates the report if it doesn't already exist.
    """

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report_path = reports_dir / f"{company.lower()}.md"

    with report_path.open("a", encoding="utf-8") as f:

        # Write title only if this is a new file
        if report_path.stat().st_size == 0:
            f.write(f"# {company} Intelligence Report\n\n")

        f.write(f"## {category}\n")
        f.write(f"**URL:** {url}\n\n")
        f.write(f"{summary}\n\n")
        f.write("---\n\n")