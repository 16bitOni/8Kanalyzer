# models.py
from pydantic import BaseModel, Field
from dataclasses import dataclass
from typing import Optional
from edgar_connector import EdgarConn

class CompanyEvent(BaseModel):
    """A company event from 8-K filing"""
    ticker: str = Field(description="The stock ticker of the company e.g. AAPL")
    name: str = Field(description="The name of the company e.g. Apple Inc.")
    date: str = Field(description="The date of the company event e.g. January 14, 2024")
    event_description: str = Field(description="The description of the company event released in the 8-K filing")

@dataclass
class CompanyNewsDependencies:
    ticker: str
    edgar: 'EdgarConn'
