from os import wait
from altair.vegalite.v4.api import value
import yfinance as yf
import streamlit as st
import pandas as pd
import time

st.write(""" ### Hi, Welcome 😭 """)
ticker = st.text_input("Enter Ticker Symbol: ")

tickerData = yf.Ticker(ticker)
tickerInfo = tickerData.info

st.title("nodebanker 🐍")
#General info
name = tickerInfo['longName']

summary = tickerInfo['longBusinessSummary']
fullTimeEmployees = tickerInfo['fullTimeEmployees']
industry = tickerInfo['industry']
sector = tickerInfo['sector']

#Prices
currentPrice = tickerInfo['currentPrice']
openPrice = tickerInfo['open']
fiftytwoLow = tickerInfo['fiftyTwoWeekLow']
fiftytwoHigh = tickerInfo['fiftyTwoWeekHigh']

#charts
tickerDf = tickerData.history(period='max')



#financial Health

debtToEquity = tickerInfo['debtToEquity']
totalDebt = tickerInfo['totalDebt']
totalAsset = tickerInfo['totalAssets']
marketCap = tickerInfo['marketCap']
bookValue = tickerInfo['bookValue']
totalRevenue = tickerInfo['totalRevenue']
totalCash = tickerInfo['totalCash']
operatingMargins = tickerInfo['operatingMargins']
profitMargins = tickerInfo['profitMargins']
revenueGrowth = tickerInfo['revenueGrowth']
roe = tickerInfo['returnOnEquity']
currentRatio = tickerInfo['currentRatio']
quickRatio = tickerInfo['quickRatio']
recommendationMean = tickerInfo['recommendationMean']
sharesShort = tickerInfo['sharesShort']
priceToBook = tickerInfo['priceToBook']
trailingEps = tickerInfo['trailingEps']

#ESG sustainability
esg = tickerData.sustainability

#News 
news = tickerData.news



st.write(""" ### Company: """, name)
st.write(""" #### Business Summary 📒 """)
st.write(summary)
st.write("Market Cap:  ${:,.2f}".format(marketCap))
st.write("Sector: ", sector)
st.write("Industry: ", industry)
st.write("full Time Employees: ", fullTimeEmployees)

#Prices Output
st.write(""" ### Prices 🏷""")
st.write("Current Price:  ${:,.2f}".format(currentPrice))
st.write("52 Week Low:  ${:,.2f}".format(fiftytwoLow))
st.write("52 Week High:  ${:,.2f}".format(fiftytwoHigh))

#Graph
st.write(""" ##### Closing Price """)
st.area_chart(tickerDf.Close)
st.write(""" ##### Volume """)
st.bar_chart(tickerDf.Volume)


#Financial Health Output
st.write(""" ### Financial Health 💰""")
st.write("Total Assets: ", totalAsset)
st.write("Total Debt: ", totalDebt)
st.write("Total Cash: ", totalCash)
st.write("Book Value", bookValue)
st.write("Total Revenue: ", totalRevenue)
st.write("Revenue Growth: ", revenueGrowth)
st.write("Operating Margins: ", operatingMargins)
st.write("Profit Margins: ", profitMargins)
st.write("Return on Equity: ", roe)
st.write("Recommendation Mean: ", recommendationMean)


#NEWS Output
st.write("## News API 📜")
st.write(news)
#st.write(news.link)

#ESG output
st.write(""" ### ESG 🌱 """)
st.write(esg)
