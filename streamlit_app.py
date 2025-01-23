import streamlit as st
import asyncio
from main import get_company_news
import pandas as pd
from datetime import datetime
import re

st.set_page_config(
    page_title="8-K Filing Analyzer",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for better styling with dark theme compatibility
st.markdown("""
    <style>
    /* Main container and text */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    
    .big-font {
        font-size: 24px !important;
        font-weight: bold;
        color: #FAFAFA;
    }
    
    /* Alert boxes */
    .stAlert {
        background-color: #262730 !important;
        color: #FAFAFA !important;
        border: 1px solid #464B5C;
    }
    
    /* Success message */
    .st-emotion-cache-16idsys {
        background-color: #044A2C !important;
        color: #A7F3D0 !important;
    }
    
    /* Error message */
    .st-emotion-cache-1y4p8pa {
        background-color: #771D1D !important;
        color: #FCA5A5 !important;
    }
    
    /* Info message */
    .st-emotion-cache-1erivf3 {
        background-color: #1E3A8A !important;
        color: #BFDBFE !important;
    }
    
    /* Warning message */
    .st-emotion-cache-1wmy9hl {
        background-color: #854D0E !important;
        color: #FDE68A !important;
    }
    
    /* DataFrame */
    .stDataFrame {
        color: #FAFAFA !important;
    }
    
    /* Card view */
    .st-emotion-cache-1v0mbdj {
        color: #FAFAFA !important;
    }
    
    /* Metric cards */
    .st-emotion-cache-12w0qpk {
        background-color: #262730 !important;
        border: 1px solid #464B5C;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background-color: #262730;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #FAFAFA;
    }
    
    /* Divider */
    hr {
        border-color: #464B5C;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<p class="big-font">8-K Filing Analyzer 📈</p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar for inputs
with st.sidebar:
    st.header("Search Settings")
    ticker = st.text_input("Enter Stock Ticker:", placeholder="e.g., AAPL, MSFT, ORCL").upper()
    analyze_button = st.button("Analyze Filings", type="primary")

def parse_date(date_str):
    """Parse date string and return in consistent format"""
    try:
        # Try direct parsing
        return datetime.strptime(date_str, '%m/%d/%Y')
    except ValueError:
        try:
            # Try to extract date using regex
            date_match = re.search(r'\d{1,2}/\d{1,2}/\d{4}', date_str)
            if date_match:
                return datetime.strptime(date_match.group(), '%m/%d/%Y')
        except:
            pass
    return None

# Main content area
if analyze_button and ticker:
    with st.spinner(f'Analyzing recent 8-K filings for {ticker}...'):
        try:
            events = asyncio.run(get_company_news(ticker))
            
            if events:
                events_data = []
                valid_dates = []
                
                for event in events:
                    parsed_date = parse_date(event.date)
                    if parsed_date:
                        valid_dates.append(parsed_date)
                        date_str = parsed_date.strftime('%m/%d/%Y')
                    else:
                        date_str = event.date  # Keep original if parsing fails
                        
                    events_data.append({
                        'Company': f"{event.name} ({event.ticker})",
                        'Date': date_str,
                        'Summary': event.event_description
                    })
                
                df = pd.DataFrame(events_data)
                
                # Display summary statistics
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Total Filings Found", len(events))
                with col2:
                    if valid_dates:
                        latest_date = max(valid_dates).strftime('%m/%d/%Y')
                        st.metric("Most Recent Filing", latest_date)
                    else:
                        st.metric("Most Recent Filing", "Date not available")
                
                # Display events in different formats
                tab1, tab2 = st.tabs(["📊 Table View", "📝 Card View"])
                
                with tab1:
                    st.dataframe(
                        df,
                        column_config={
                            "Company": st.column_config.TextColumn("Company"),
                            "Date": st.column_config.DateColumn("Filing Date"),
                            "Summary": st.column_config.TextColumn("Summary", width="large"),
                        },
                        hide_index=True,
                    )
                
                with tab2:
                    for event in events:
                        with st.container():
                            st.markdown(f"""
                            #### 🏢 {event.name} ({event.ticker})
                            **Date:** {event.date}  
                            **Summary:** {event.event_description}
                            """)
                            st.divider()
                
            else:
                st.warning(f"No recent 8-K filings found for {ticker}")
                
        except Exception as e:
            st.error(f"Error analyzing filings: {str(e)}")
else:
    # Display instructions when no ticker is entered
    st.info("""
        👈 Enter a stock ticker in the sidebar to get started!
        
        This tool analyzes recent 8-K filings and provides AI-generated summaries of key events.
        """)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p style='color: #888888; font-size: 14px;'>
            Powered by Gemini AI & SEC EDGAR Database
        </p>
    </div>
    """, unsafe_allow_html=True) 