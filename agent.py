import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from schema import MarketReport

# Load keys from .env
load_dotenv()

# Define the Agent
research_agent = Agent(
    'google-gla:gemini-2.0-flash',
    result_type=MarketReport,
    system_prompt=(
        "You are a professional Market Research Agent. "
        "Your goal is to find accurate news and pricing data using the provided tools. "
        "Always provide source URLs for every fact."
    )
)

print("Agent initialized with MarketReport schema.")