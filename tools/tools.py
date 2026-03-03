'''



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

        '''

import os
import httpx
from dotenv import load_dotenv

load_dotenv()


'''


async def search_market_data(query: str) -> str:
    # 1. Correct way to get the key
    tavily_api_key = os.getenv('TAVILY_API_KEY')
    
    if not tavily_api_key:
        print("DEBUG: API Key Missing!")
        return "Error: TAVILY_API_KEY is not set."

    tavily_url = "https://api.tavily.com/search"
    tavily_payload = {
        "api_key": tavily_api_key,
        "query": query,
        "search_depth": "smart"
    }
    
    # 2. Add a timeout to prevent infinite waiting
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            print(f"DEBUG: Calling Tavily for: {query}...")
            response = await client.post(tavily_url, json=tavily_payload)
            response.raise_for_status() # This will catch 401/403 errors
            
            tavily_data = response.json()
            results = tavily_data.get("results", [])
            
            if not results:
                return "Search returned 0 results."

            # 3. Format into a clear string for the AI
            context = ""
            for r in results:
                context += f"URL: {r['url']}\nInfo: {r['content']}\n---\n"
            return context
            
        except Exception as e:
            print(f"DEBUG: Tool Error: {e}")
            return f"The search tool failed with error: {str(e)}"
'''


async def search_market_data(query: str) -> str:
    # Use os.getenv to safely get the key
    api_key = os.getenv('TAVILY_API_KEY')
    
    if not api_key:
        return "Error: TAVILY_API_KEY missing from .env"

    url = "https://api.tavily.com/search"
    # Keeping it minimal to avoid 400 errors
    payload = {
        "api_key": api_key,
        "query": query,
        "search_depth": "basic", # Use basic for now to save credits
        "max_results": 3
    }
    
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post(url, json=payload)
        if response.status_code != 200:
            # This will help us see the EXACT reason for the 400
            return f"Tavily Error {response.status_code}: {response.text}"
            
        data = response.json()
        results = data.get("results", [])
        return "\n".join([f"Source: {r['url']}\n{r['content']}" for r in results])