from dotenv import load_dotenv
import os
load_dotenv()
from rich import print
import requests

from langchain_mistralai import ChatMistralAI
from bs4 import BeautifulSoup
from tavily import TavilyClient
from langchain.tools import tool

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def webSearch(query : str) -> str:
    """Search the web for recent and reliable information on a topic . Returns Titles , URLs and snippets."""
    results = tavily.search(query=query,max_results=5)
    news_list = []
    for r in results['results']:
       news_list.append(
           f"Title : {r['title']}\nURL : {r['url']}\n Snippet : {r['content'][:300]}\n"
       )

    return "\n".join(news_list)


@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        # Header means a user is accessing the webpage not beautiful soup


        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            # decompose means take only the content not the tags

            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:30000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
        

# query = input("ENTER url : ")
# result = scrape_url.invoke(query)


# print(result)

# @tool
# def rewrite(report : str,feedback : str) -> str:
#     """"""