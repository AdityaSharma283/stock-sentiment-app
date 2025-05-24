import streamlit as st
from fetch_data import fetch_news
from gemini_summary import get_sentiment_summary
from chart_utils import plot_stock_chart
from sentiment_model import predict_sentiment

st.set_page_config(page_title="Stock Sentiment Analyzer", layout="centered")
st.title("📊 Indian Stock Market Sentiment Analyzer")

# Optional: Dropdown with common NSE tickers
common_tickers = [
    "TCS.NS", "RELIANCE.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "SBIN.NS", "WIPRO.NS", "HINDUNILVR.NS", "LT.NS", "AXISBANK.NS"
]

ticker = st.selectbox("Choose Stock Ticker:", common_tickers)
st.markdown("💡 Tip: Indian tickers use `.NS` (NSE) or `.BO` (BSE), e.g., `TCS.NS`, `RELIANCE.NS`.")

if ticker:
    st.write("🔄 Fetching latest data...")

    try:
        news_headlines, prices = fetch_news(ticker)
    except Exception as e:
        st.error(f"❌ Failed to fetch data: {e}")
        st.stop()

    # Optional: Show fetched headlines for debugging
    # st.write("Fetched headlines:", news_headlines)

    # Validate headlines
    if not news_headlines or not isinstance(news_headlines, list) or not all(isinstance(h, str) and h.strip() for h in news_headlines):
        st.error("❌ Error: Invalid or empty headlines fetched.")
        st.stop()

    try:
        summary = get_sentiment_summary(news_headlines)
        predictions = predict_sentiment(news_headlines)
    except Exception as e:
        st.error(f"❌ Prediction or summary failed: {e}")
        st.stop()

    st.subheader("🧠  AI Summary")
    st.write(summary)

    st.subheader("🗞️ Predicted Sentiments")
    for h, s in zip(news_headlines, predictions):
        sentiment = "Positive" if s == 1 else "Negative"
        st.write(f"📰 {h} — **{sentiment}**")

    st.subheader("📈 Price Chart")
    try:
        plot_stock_chart(prices)
    except Exception as e:
        st.error(f"❌ Failed to plot chart: {e}")

