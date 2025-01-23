# edgar_connector.py
from edgar import *   
from typing import Optional
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

class EdgarConn:
    def __init__(self):
        set_identity('Subhadipmondal789@gmail.com')

    def _analyze_8k(eight_k):  # Added 'self' parameter
        """Analyze 8-K specific content"""
        return {
            'items':{f"{i}": eight_k[index].strip() for i, index in enumerate(eight_k.items)} if hasattr(eight_k, 'items') else None
            }
    @classmethod
    async def latest_8k(cls, *, ticker: str) -> Optional[str]:
        """Fetches the latest 8-K filing for a given ticker"""
        try:
            company = Company(ticker)
            if not company:
                return None
            today = datetime.today()
            one_year_ago = (today - relativedelta(years=1)).strftime('%Y-%m-%d') 
            filings_8k = list(company.get_filings(form=['8-K'], date=one_year_ago + ':'))
            filing_analysis = []    
            for filing in filings_8k:
                filing_obj = filing.obj()
                if filing_obj:
                    analysis = cls._analyze_8k(filing_obj)
                    filing_analysis.append(analysis)
            return filing_analysis
        
        except Exception as e:
            print(f"Error fetching 8-K for {ticker}: {str(e)}")
            return None