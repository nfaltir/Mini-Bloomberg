import yfinance as yf
import streamlit as st
import pandas as pd


#streamlit config

st.set_page_config(page_title="Stock Report", page_icon="🌱")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
         
            footer {visibility: hidden;}
           
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


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
    revPerEmployee = round(totalRevenue/fullTimeEmployees, 2)

    #Recommendations
      
    recommendations = tickerData.recommendations['To Grade'].value_counts()
    
    #ESG sustainability
    esg = tickerData.sustainability

    #News 
    news = tickerData.news


    st.markdown("<hr><br>", unsafe_allow_html=True)
    st.write(""" ### Company: """, name)
    st.write(""" #### Business Summary 📒 """)
    st.markdown(f"<p style='text-align:justify;'>{summary}</p>", unsafe_allow_html=True)



    st.markdown("<br>", unsafe_allow_html=True)
    companyMetaData = {'Market Cap':[f'${marketCap:,}'],'Sector':[sector],'Industry':[industry], 'Fulltime Employees':[f'{fullTimeEmployees:,}'],\
         'Revenue Per Employee':[f'${revPerEmployee:,}']}
    df_meta_data = pd.DataFrame(data=companyMetaData)
    st.table(df_meta_data.reset_index(drop=True))




    st.markdown("<hr><br>", unsafe_allow_html=True)
    #Prices Output
    st.write(""" ### Prices 🏷""")
    st.write("Current Price:  ${:,.2f}".format(currentPrice))
    st.write("52 Week Low:  ${:,.2f}".format(fiftytwoLow))
    st.write("52 Week High:  ${:,.2f}".format(fiftytwoHigh))
    st.markdown("<hr><br>", unsafe_allow_html=True)
    
    #Graph
    st.write(""" ##### Closing Price """)
    st.area_chart(tickerDf.Close)

    st.write(""" ##### Volume """)
    st.bar_chart(tickerDf.Volume)

    st.markdown("<hr><br>", unsafe_allow_html=True)
    #Financial Health Output
    st.write(""" ### Financial Health 💰""")
    st.write("Total Assets: ", totalAsset)
    st.write("Total Debt: ${:,.2f}".format(totalDebt))
    st.write("Total Cash: ${:,.2f}".format(totalCash))
    st.write("Book Value", bookValue)

    st.write("Total Revenue:  ${:,.2f}".format(totalRevenue))
   

    st.write("Revenue Growth: ", revenueGrowth)
    st.write("Operating Margins: ", operatingMargins)
    st.write("Profit Margins: ", profitMargins)
    st.write("Return on Equity: ", roe)
    st.write("Recommendation Mean: ", recommendationMean)
    st.markdown("<hr><br>", unsafe_allow_html=True)

  
      
   

    #Recommendations Output
    st.write("### Street Total Recommendations 🏛")
    st.table(recommendations)
    st.markdown("<hr><br>", unsafe_allow_html=True)

    #ESG output
    #st.write(""" ### ESG 🌱 """)
    #try:
     #   st.write(esg)
    #except Exception as e:
     #   print (f"Error: {e}")
      #  st.warning(e)

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Major Holders")
    st.write(tickerData.institutional_holders)
    st.markdown("<hr><br>", unsafe_allow_html=True)

      #NEWS Output
    st.subheader("Recent News")
    for i in news:
        st.write(f'{i["title"]}\n{i["link"]}')
    
