import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from schema import MarketReport
from tools.tools import search_market_data

# Load keys from .env
load_dotenv()

# Define the Agent
research_agent=Agent(
    'google-gla:gemini-2.5-flash-lite',
    output_type=MarketReport,
    deps_type=None,            # <--- Explicitly tell the agent we have no dependencies
    system_prompt=(
        "You are a professional Market Research Agent. "
        "Your goal is to find accurate news and pricing data using the provided tools. "
        "Always provide source URLs for every fact."
    )
)

# print("Agent initialized with MarketReport schema.")

# Register the tool so the Agent knows it exists
@research_agent.tool_plain
async def web_search(query:str) -> str:
    """
    Finds real-time market data and news. Use this for pricing and competitor info.
    """
    return await search_market_data(query)

# This block allows you to run the script from the terminal
if __name__ == "__main__":
    print("Starting Research...")
    # We use run_sync for a simple terminal script
    result = research_agent.run_sync("Research the current market price and latest news for the Nvidia RTX 5090.")
    
    print("\n--- FINAL REPORT ---",result)
    print("\n--- REPORT Data---",result.output)
    report=result.output
    print(f"Summary: {report.summary}")
    print(f"\nRecent Headlines:")
    for headline in report.news_headlines:
        print(f"- {headline}")
    print(f"\nPricing Status:")
    for item in report.pricing_data:
        print(f"- {item.fact} (Source: {item.source_url})")