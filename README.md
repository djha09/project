# AI Research Agent

A simple AI research pipeline that searches for information, scrapes a relevant source, generates a report, and improves it using a critic and rewriter.

## How It Works

```text
Topic
  ↓
Search Agent
  ↓
Scrape Agent
  ↓
Writer
  ↓
Critic
  ↓
Rewriter
  ↓
Final Review
```

## Features

- Searches for recent information
- Scrapes a relevant source
- Generates a research report
- Reviews the report with a critic
- Rewrites the report based on feedback
- Reviews the rewritten report

## Project Structure

```text
project/
├── agents.py
├── main.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

```bash
git clone <repository-url>
cd <project-folder>
pip install -r requirements.txt
```

Create a `.env` file and add the required API keys.

## Usage

Run the project:

```bash
python main.py
```

Enter a research topic when prompted:

```text
Enter a research topic: Artificial Intelligence in Healthcare
```

The pipeline will search, scrape, write, critique, and rewrite the report.

## Main Function

```python
runSearch(topic: str) -> dict
```

The function returns:

```python
{
    "search_results": ...,
    "scraped_content": ...,
    "report": ...,
    "feedback": ...,
    "rewrite": ...
}
```

## Requirements

- Python 3.10+
- Required API keys
- Dependencies listed in `requirements.txt`

## License

MIT
