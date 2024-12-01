import yfinance as yf
import datetime
from datetime import datetime, timedelta

one_year_ago = datetime.today() - timedelta(days=365)
formatted_date = one_year_ago.strftime("%Y-%m-%d")

def fetch_data(tickers, start_date=None, end_date=None):
    if start_date is None:
        start_date = (datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")
    if end_date is None:
        end_date = datetime.today().strftime("%Y-%m-%d")
    
    data = {}
    
    for ticker in tickers:
        stock = yf.download(ticker, start=start_date, end=end_date)
        data[ticker] = stock
  
    return data

def filter_stocks(data, min_volatility=0.02, min_avg_volume=500000):
    selected_stocks = []
    
    for ticker, stock_data in data.items():
        # Calculate daily returns
        stock_data['Daily_Return'] = stock_data['Adj Close'].pct_change()
        
        # Calculate volatility (standard deviation of daily returns)
        volatility = stock_data['Daily_Return'].std()  # This should be a scalar
        
        # Average daily volume
        avg_volume = stock_data['Volume'].mean()  # This should be a scalar
        
        # If the stock meets criteria, add it to the selection
        if volatility > min_volatility and avg_volume > min_avg_volume:
            selected_stocks.append(ticker)
    
    return selected_stocks

tickers = ['AAPL', 'TSLA', 'GOOGL', 'AMZN', 'MSFT']
stock_data = fetch_data(tickers)
selected_stocks = filter_stocks(stock_data)

print("Selected stocks based on criteria:", selected_stocks)
