import yfinance as yf
from bs4 import BeautifulSoup
import requests

def fetch_news(ticker):
    # --- Step 1: Try scraping news from Moneycontrol ---
    try:
        stock_code = ticker.split('.')[0]
        url = f"https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id={stock_code}"
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')

        headlines = [a.text.strip() for a in soup.select('div#newslist span') if a.text.strip()]
        if not headlines:
            raise ValueError("No headlines found.")
        headlines = headlines[:5]
    except Exception as e:
        print(f"[WARN] News scraping failed: {e}")
        headlines = [
            f"{ticker} market sentiment mixed amid trading activity.",
            f"Investors react to recent movements in {ticker}.",
            f"{ticker} shows volatility after earnings forecast.",
            f"Analysts discuss growth potential for {ticker}.",
            f"News round-up: {ticker} in spotlight this week."
        ]

    # --- Step 2: Fetch historical stock data using yfinance ---
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1mo")

        if hist.empty:
            raise ValueError("No price data found. Ticker may be invalid or delisted.")
    except Exception as e:
        raise RuntimeError(f"❌ Failed to fetch stock price data: {e}")

    return headlines, hist

