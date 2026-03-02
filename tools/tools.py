import os
import httpx
from dotenv import load_dotenv

load_dotenv()

async def search_market_data(query:str) -> str:  #send the query param of type string and func returns the result of type str
    """
    Searches the live web for market data, pricing, and news.
    """
    tavily_api_key= load_dotenv('TAVILY_API_KEY')
    tavily_url = "https://api.tavily.com/search"
    tavily_payload = {
        "api_key": tavily_api_key,
        "query": query,
        "search_depth": "smart",
        "include_answer": True
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(tavily_url,json=tavily_payload)
        tavily_data = response.json()
        return str(tavily_data .get("results", "No results found.")) #We are looking into the dictionary for a key called "results". If the search found nothing, it defaults to "No results found.".