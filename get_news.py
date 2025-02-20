import requests

def get_ticker_news(ticker, num_stories=10):
    url = f"https://api.tickertick.com/feed?q=z:{ticker}&n={num_stories}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"
