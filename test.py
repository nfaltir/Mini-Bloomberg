import yfinance as yf
import pandas as pd
import numpy as np
import streamlit as st

ticker = st.text_input("Enter Ticker Symbol: ")
tickerObj = yf.Ticker(ticker)
tickerData = tickerObj.info
if len (ticker) > 0:
    
    recommendations = tickerObj.recommendations['To Grade'].value_counts()
    st.table(recommendations)
    st.line_chart(tickerObj.history)