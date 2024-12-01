import finnhub
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Set up Finnhub API Key
finnhub_client = finnhub.Client(api_key="ct6e09pr01qmbqorp5bgct6e09pr01qmbqorp5c0")

# Helper function to get P/E, Debt/Equity, and earnings growth from Finnhub
def get_fundamentals(ticker):
    try:
        profile = finnhub_client.company_profile2(symbol=ticker)
        pe_ratio = profile.get('peRatio', None)
        debt_to_equity = profile.get('debtToEquity', None)
        earnings_growth = profile.get('earningsGrowth', None)
        
        return pe_ratio, debt_to_equity, earnings_growth
    except Exception as e:
        print(f"Error fetching fundamentals for {ticker}: {e}")
        return None, None, None

# Fetch stock data from Yahoo Finance for moving averages and volatility
def fetch_price_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Fetch a list of S&P 500 tickers (you can use other sources if needed)
def get_sp500_tickers():
    # List of S&P 500 tickers (source: Wikipedia or CSV file)
    sp500_tickers = [
        'MMM', 'ACE', 'ABT', 'ANF', 'ACN', 'ADBE', 'AMD', 'AES', 'AET', 'AFL', 'A', 'GAS', 'APD', 'ARG', 'AKAM', 'AA', 'ALXN', 'ATI', 'AGN', 'ALL', 'ANR', 'ALTR', 'MO', 'AMZN', 'AEE', 'AEP', 'AXP', 'AIG', 'AMT', 'AMP', 'ABC', 'AMGN', 'APH', 'APC', 'ADI', 'AON', 'APA', 'AIV', 'APOL', 'AAPL', 'AMAT', 'ADM', 'AIZ', 'T', 'ADSK', 'ADP', 'AN', 'AZO', 'AVB', 'AVY', 'AVP', 'BHI', 'BLL', 'BAC', 'BK', 'BCR', 'BAX', 'BBT', 'BEAM', 'BDX', 'BBBY', 'BMS', 'BRK.B', 'BBY', 'BIG', 'BIIB', 'BLK', 'HRB', 'BMC', 'BA', 'BWA', 'BXP', 'BSX', 'BMY', 'BRCM', 'BF.B', 'CHRW', 'CA', 'CVC', 'COG', 'CAM', 'CPB', 'COF', 'CAH', 'CFN', 'KMX', 'CCL', 'CAT', 'CBG', 'CBS', 'CELG', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW', 'CHK', 'CVX', 'CMG', 'CB', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CTXS', 'CLF', 'CLX', 'CME', 'CMS', 'COH', 'KO', 'CCE', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CSC', 'CAG', 'COP', 'CNX', 'ED', 'STZ', 'CBE', 'GLW', 'COST', 'CVH', 'COV', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DF', 'DE', 'DELL', 'DNR', 'XRAY', 'DVN', 'DV', 'DO', 'DTV', 'DFS', 'DISCA', 'DLTR', 'D', 'RRD', 'DOV', 'DOW', 'DPS', 'DTE', 'DD', 'DUK', 'DNB', 'ETFC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMC', 'EMR', 'ESV', 'ETR', 'EOG', 'EQT', 'EFX', 'EQR', 'EL', 'EXC', 'EXPE', 'EXPD', 'ESRX', 'XOM', 'FFIV', 'FDO', 'FAST', 'FII', 'FDX', 'FIS', 'FITB', 'FHN', 'FSLR', 'FE', 'FISV', 'FLIR', 'FLS', 'FLR', 'FMC', 'FTI', 'F', 'FRX', 'FOSL', 'BEN', 'FCX', 'FTR', 'GME', 'GCI', 'GPS', 'GD', 'GE', 'GIS', 'GPC', 'GNW', 'GILD', 'GS', 'GT', 'GOOG', 'GWW', 'HAL', 'HOG', 'HAR', 'HRS', 'HIG', 'HAS', 'HCP', 'HCN', 'HNZ', 'HP', 'HES', 'HPQ', 'HD', 'HON', 'HRL', 'HSP', 'HST', 'HCBK', 'HUM', 'HBAN', 'ITW', 'IR', 'TEG', 'INTC', 'ICE', 'IBM', 'IFF', 'IGT', 'IP', 'IPG', 'INTU', 'ISRG', 'IVZ', 'IRM', 'JBL', 'JEC', 'JDSU', 'JNJ', 'JCI', 'JOY', 'JPM', 'JNPR', 'K', 'KEY', 'KMB', 'KIM', 'KMI', 'KLAC', 'KSS', 'KFT', 'KR', 'LLL', 'LH', 'LRCX', 'LM', 'LEG', 'LEN', 'LUK', 'LXK', 'LIFE', 'LLY', 'LTD', 'LNC', 'LLTC', 'LMT', 'L', 'LO', 'LOW', 'LSI', 'MTB', 'M', 'MRO', 'MPC', 'MAR', 'MMC', 'MAS', 'MA', 'MAT', 'MKC', 'MCD', 'MHP', 'MCK', 'MJN', 'MWV', 'MDT', 'MRK', 'MET', 'PCS', 'MCHP', 'MU', 'MSFT', 'MOLX', 'TAP', 'MON', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MUR', 'MYL', 'NBR', 'NDAQ', 'NOV', 'NTAP', 'NFLX', 'NWL', 'NFX', 'NEM', 'NWSA', 'NEE', 'NKE', 'NI', 'NE', 'NBL', 'JWN', 'NSC', 'NTRS', 'NOC', 'NU', 'NRG', 'NUE', 'NVDA', 'NYX', 'ORLY', 'OXY', 'OMC', 'OKE', 'ORCL', 'OI', 'PCAR', 'PLL', 'PH', 'PDCO', 'PAYX', 'BTU', 'JCP', 'PBCT', 'POM', 'PEP', 'PKI', 'PRGO', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PXD', 'PBI', 'PCL', 'PNC', 'RL', 'PPG', 'PPL', 'PX', 'PCP', 'PCLN', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 'QEP', 'PWR', 'QCOM', 'DGX', 'RRC', 'RTN', 'RHT', 'RF', 'RSG', 'RAI', 'RHI', 'ROK', 'COL', 'ROP', 'ROST', 'RDC', 'R', 'SWY', 'SAI', 'CRM', 'SNDK', 'SCG', 'SLB', 'SNI', 'STX', 'SEE', 'SHLD', 'SRE', 'SHW', 'SIAL', 'SPG', 'SLM', 'SJM', 'SNA', 'SO', 'LUV', 'SWN', 'SE', 'S', 'STJ', 'SWK', 'SPLS', 'SBUX', 'HOT', 'STT', 'SRCL', 'SYK', 'SUN', 'STI', 'SYMC', 'SYY', 'TROW', 'TGT', 'TEL', 'TE', 'THC', 'TDC', 'TER', 'TSO', 'TXN', 'TXT', 'HSY', 'TRV', 'TMO', 'TIF', 'TWX', 'TWC', 'TIE', 'TJX', 'TMK', 'TSS', 'TRIP', 'TSN', 'TYC', 'USB', 'UNP', 'UNH', 'UPS', 'X', 'UTX', 'UNM', 'URBN', 'VFC', 'VLO', 'VAR', 'VTR', 'VRSN', 'VZ', 'VIAB', 'V', 'VNO', 'VMC', 'WMT', 'WAG', 'DIS', 'WPO', 'WM', 'WAT', 'WPI', 'WLP', 'WFC', 'WDC', 'WU', 'WY', 'WHR', 'WFM', 'WMB', 'WIN', 'WEC', 'WPX', 'WYN', 'WYNN', 'XEL', 'XRX', 'XLNX', 'XL', 'XYL', 'YHOO', 'YUM', 'ZMH', 'ZION'
    ]  # Sample tickers, extend this list for more tickers
    return sp500_tickers

# Function to filter stocks based on the criteria (fundamentals + price action + volatility)
def filter_stocks(tickers, min_volatility=0.02, min_avg_volume=500000, min_pe=10, max_pe=30, max_debt_to_equity=1.5, min_earnings_growth=0.05):
    selected_stocks = []
    
    for ticker in tickers:
        # Get fundamentals data
        pe_ratio, debt_to_equity, earnings_growth = get_fundamentals(ticker)
        
        # Check fundamental criteria
        if pe_ratio is not None and debt_to_equity is not None and earnings_growth is not None:
            if min_pe <= pe_ratio <= max_pe and debt_to_equity < max_debt_to_equity and earnings_growth >= min_earnings_growth:
                
                # Fetch price data for 6-month price action
                end_date = datetime.today()
                start_date = end_date - timedelta(days=180)  # Last 6 months
                price_data = fetch_price_data(ticker, start_date, end_date)
                
                # Calculate daily returns and volatility (standard deviation of daily returns)
                price_data['Daily_Return'] = price_data['Adj Close'].pct_change()
                volatility = price_data['Daily_Return'].std()
                
                # Calculate average daily volume
                avg_volume = price_data['Volume'].mean()
                
                # Calculate 50-day moving average
                price_data['50_MA'] = price_data['Adj Close'].rolling(window=50).mean()
                
                # Check if the stock is above its 50-day moving average
                is_above_50ma = price_data['Adj Close'][-1] > price_data['50_MA'][-1]
                
                # Calculate average daily price movement over the past 6 months
                avg_daily_movement = price_data['Daily_Return'].abs().mean() * 100  # in percentage
                
                # Apply additional filtering conditions based on volatility and moving averages
                if volatility > min_volatility and avg_volume > min_avg_volume and avg_daily_movement < 2 and is_above_50ma:
                    selected_stocks.append(ticker)
    
    return selected_stocks

# Get the list of S&P 500 tickers
tickers = get_sp500_tickers()
print("Tickers to analyze:", tickers)

# Filter stocks based on the criteria (fundamentals + price action + volatility)
selected_stocks = filter_stocks(tickers)

print("Selected stocks based on criteria:", selected_stocks)
