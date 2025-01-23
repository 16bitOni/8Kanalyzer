# agent.py
import google.generativeai as genai
import os
from dataclasses import asdict
from config import GOOGLE_API_KEY

# Configure Gemini

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

async def analyze_8k(ticker: str, filing_text: str) -> dict:
    """Analyze 8-K filing using Gemini"""
    prompt = f"""
    Analyze this 8-K filing for {ticker} and provide a concise summary in this exact format:
    COMPANY: [company name only without ticker]
    DATE: [event date in MM/DD/YYYY format, if exact date is not available, use filing date]
    SUMMARY: [brief, tweet-style summary under 300 characters]
    
    Important: For DATE, use MM/DD/YYYY format (e.g., 01/15/2024). If multiple dates are mentioned, use the primary event date.
    
    Filing text:
    {filing_text}
    """
    
    response = model.generate_content(prompt)
    lines = response.text.split('\n')
    
    # Parse the structured response
    parsed_data = {}
    for line in lines:
        if line.startswith('COMPANY:'):
            parsed_data['name'] = line.replace('COMPANY:', '').strip()
        elif line.startswith('DATE:'):
            parsed_data['date'] = line.replace('DATE:', '').strip()
        elif line.startswith('SUMMARY:'):
            parsed_data['event_description'] = line.replace('SUMMARY:', '').strip()
    
    return {
        "ticker": ticker,
        "name": parsed_data.get('name', ''),
        "date": parsed_data.get('date', ''),
        "event_description": parsed_data.get('event_description', '')
    }