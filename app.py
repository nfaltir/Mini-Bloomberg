from os import wait
from altair.vegalite.v4.api import value
import yfinance as yf
import streamlit as st
import pandas as pd
import time

st.markdown("<h1 style='text-align: center; color: #4C4C6D;'> Stock Report 🌋</h1>", unsafe_allow_html=True)
st.write("<hr><br>", unsafe_allow_html=True)
ticker = st.text_input("Enter Ticker Symbol:")
st.button("Generate Report")



if len(ticker) > 0:

    tickerData = yf.Ticker(ticker)
    tickerInfo = tickerData.info

 
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

    #Recommendations
      
    recommendations = tickerData.recommendations['To Grade'].value_counts()
    
    #ESG sustainability
    esg = yf.Ticker(ticker).sustainability

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

    #Recommendations Output
    st.write("### Street Total Recommendations 🏛")
    st.dataframe(recommendations)

    #ESG output
    st.write(""" ### ESG 🌱 """)
    st.write(esg)
