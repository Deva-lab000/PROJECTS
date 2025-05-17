import yfinance as yf
import pandas as pd

def get_stock_data(ticker: str, period='1mo', interval='1d'):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    return hist.reset_index()

if __name__ == "__main__":
    df = get_stock_data("AAPL")
    print(df.head())