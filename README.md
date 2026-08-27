AI Research Agent

A simple AI research pipeline that searches for information, scrapes a relevant source, generates a report, and improves it using a critic and rewriter.

How it works
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

Features
Searches for recent information
Scrapes a relevant source
Generates a research report
Reviews the report with a critic
Rewrites the report based on feedback
Reviews the rewritten report
Project Structure
project/
├── agents.py
├── main.py
├── requirements.txt
├── .env
└── README.md

Installation

Clone the repository and install the dependencies:

git clone <repository-url>
cd <project-folder>
pip install -r requirements.txt


Create a .env file and add the required API keys.

Usage

Run:

python main.py


Enter a topic when prompted:

Enter a research topic: Artificial Intelligence in Healthcare


The pipeline will then search, scrape, write, critique, and rewrite the report.

Main Function
runSearch(topic: str) -> dict


It returns the results from each step:

{
    "search_results": ...,
    "scraped_content": ...,
    "report": ...,
    "feedback": ...,
    "rewrite": ...
}

Requirements
Python 3.10+
Required API keys
Dependencies listed in requirements.txt
License

MIT
