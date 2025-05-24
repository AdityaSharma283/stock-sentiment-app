import plotly.graph_objs as go
import streamlit as st

def plot_stock_chart(prices):
    fig = go.Figure(data=[go.Candlestick(
        x=prices.index,
        open=prices['Open'],
        high=prices['High'],
        low=prices['Low'],
        close=prices['Close']
    )])
    st.plotly_chart(fig)
