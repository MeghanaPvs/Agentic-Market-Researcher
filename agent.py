import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from schema import MarketReport

# Load keys from .env
load_dotenv()

# Define the Agent
research_agent = Agent(
    'openai:gpt-4o',
    result_type=MarketReport,
    system_prompt="You are a real-time market researcher. Use tools to find pricing and news."
)

print("Agent initialized with MarketReport schema.")