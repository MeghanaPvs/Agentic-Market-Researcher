from pydantic import BaseModel, Field
from typing import List, Optional

class ResearchItem(BaseModel):
    """ Represents a specific data point found during web research.
    Used to ensure every fact has a verifiable source.
    """
    source_url: str = Field(description="The exact web link where the information was retrieved.")
    fact: str = Field(description="A specific, verifiable piece of information regarding pricing or news.")

class MarketReport(BaseModel):
    """The final structured report the agent must produce."""
    company_name: str = Field(description="The formal name of the company being researched.")
    summary: str = Field(
        description="A concise, 3-sentence executive summary of the company's current market position."
    )
    pricing_data: List[ResearchItem] = Field(
        description="A collection of verified pricing points found across different sources."
    )
    news_headlines: List[str] = Field(
        description="A list of the most impactful news headlines from the last 6 months."
    )