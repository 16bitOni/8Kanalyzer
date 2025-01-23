import asyncio
from models import CompanyEvent
from edgar_connector import EdgarConn
from agent import analyze_8k

async def get_company_news(ticker: str) -> None:
    """Get and print the latest news for a company."""
    try:
        # Initialize the Edgar connection
        edgar = EdgarConn()
        filings_list = await edgar.latest_8k(ticker=ticker)
        
        if filings_list:
            events = []  # Store all events for further processing
            
            # Process each filing
            for filing in filings_list:
                items = filing.get('items', {})
                
                if not items:
                    continue
                
                # Process each item in the filing
                for item_key, item_text in items.items():
                    try:
                        # Get the structured data using Gemini
                        event_data = await analyze_8k(ticker, item_text)
                        
                        # Create a CompanyEvent instance
                        company_event = CompanyEvent(**event_data)
                        events.append(company_event)
                        
                        # Format tweet-style output
                        tweet = f"🔔 {company_event.name} ({company_event.ticker}) Update:\n"
                        tweet += f"📅 {company_event.date}\n"
                        tweet += f"📝 {company_event.event_description}"
                        
                        print("\n" + "="*50)
                        print(tweet)
                        print("="*50)
                        
                    except Exception as e:
                        print(f"Error processing Item {item_key}: {str(e)}")
            
            return events  # Return events for further processing if needed
            
        else:
            print(f"No recent 8-K filings found for {ticker}.")
            return None
            
    except Exception as e:
        print(f"Error getting news for {ticker}: {str(e)}")
        return None

if __name__ == "__main__":
    ticker = input("Enter company ticker (e.g., ORCL): ")
    asyncio.run(get_company_news(ticker))
