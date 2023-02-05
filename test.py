import yfinance as yf

ticker = yf.Ticker("GOOGL")
info = ticker.info
print(info.keys())