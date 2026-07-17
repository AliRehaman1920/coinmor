# Competitive Intelligence Monitor

An AI-powered Competitive Intelligence Monitor built with **Python**, **LangGraph**, and **OpenAI**.

The goal of this project is to automatically monitor competitor websites, detect meaningful changes, and generate concise AI-powered summaries so users can stay informed without manually checking websites.

> **Note:** This is an early/basic version of the project. More features and improvements are planned.

---

## Features

- Add companies to monitor
- Automatically discover important pages on a company's website
- Collect webpage content
- Store webpage snapshots
- Detect content changes between runs
- Generate AI-powered summaries of meaningful changes
- Create Markdown reports for each monitored company

---

## Workflow

```
Company
    ↓
Discovery
    ↓
Collection
    ↓
Snapshots
    ↓
Intelligence
    ↓
Reports
```

---

## Tech Stack

- Python
- LangGraph
- LangChain
- Groq API
- Llama 3.3 70B
- Playwright
- BeautifulSoup
- Requests
---

## Project Structure

```
collection/
discovery/
graph/
reports/
snapshot/
snapshots/

main.py
requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

Move into the project directory:

```bash
cd <repository-name>
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```text
GROQ_API_KEY=your_groq_api_key_here

Run the project:

```bash
python main.py
```

---

## How to Use

When the application starts, you'll see a menu:

```
1. Add company
2. Monitor existing companies
3. Exit
```

### Add Company

- Enter the company name.
- Enter the company's homepage URL.
- The Discovery workflow automatically finds important pages to monitor.

### Monitor Existing Companies

Runs the complete monitoring pipeline:

- Collection
- Snapshot comparison
- AI analysis
- Report generation

Generated reports are saved inside the `reports/` directory.

---

## Future Improvements

This project is still under active development. Planned additions include:

- PostgreSQL database support
- APScheduler for automatic scheduled monitoring
- Email notifications
- News monitoring
- Job posting monitoring
- Press release monitoring
- Better change detection
- Structured LLM outputs
- Docker support
- Web dashboard
- Multi-user support
- Smarter discovery workflow
- Report generation with richer insights

---

## Contributing

Contributions, suggestions, and feedback are always welcome.

If you'd like to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Open a Pull Request.

---

## License

This project is open source and intended for learning and educational purposes.

---

## Acknowledgements

## Acknowledgements

This project was designed and implemented by me with some development assistance from **ChatGPT (OpenAI)**, including code review, debugging, and implementation guidance.