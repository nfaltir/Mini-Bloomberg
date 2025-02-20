import yfinance as yf
import streamlit as st
import pandas as pd
from get_news import get_ticker_news

# Streamlit config
st.set_page_config(page_title="Stock Report", page_icon="🌱")

# Hide Streamlit style
st.markdown("""
    <style>
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #4C4C6D;'>Stock Report 🌋</h1>", unsafe_allow_html=True)

# User Input
ticker = st.text_input("Enter Ticker Symbol:")
if st.button("Generate Report") and ticker:
    try:
        ticker_data = yf.Ticker(ticker)
        ticker_info = ticker_data.info

        # General Info
        name = ticker_info.get('longName', 'N/A')
        summary = ticker_info.get('longBusinessSummary', 'N/A')
        website = ticker_info.get('website', 'N/A')
        full_time_employees = ticker_info.get('fullTimeEmployees', 'N/A')
        industry = ticker_info.get('industry', 'N/A')
        sector = ticker_info.get('sector', 'N/A')
        market_cap = ticker_info.get('marketCap', 'N/A')
        total_revenue = ticker_info.get('totalRevenue', 'N/A')
        total_assets = ticker_info.get('totalDebt', 0) + (ticker_info.get("bookValue", 0) * ticker_info.get("sharesOutstanding", 0))
        rev_per_employee = total_revenue / full_time_employees if isinstance(total_revenue, (int, float)) and isinstance(full_time_employees, (int, float)) else 'N/A'

        # Prices
        current_price = ticker_info.get('currentPrice', 'N/A')
        fiftytwo_low = ticker_info.get('fiftyTwoWeekLow', 'N/A')
        fiftytwo_high = ticker_info.get('fiftyTwoWeekHigh', 'N/A')

        # Target Prices
        recomm_key = ticker_info.get('recommendationKey', 'N/A')
        mean_target = ticker_info.get('targetMeanPrice', 'N/A')
        low_target = ticker_info.get('targetLowPrice', 'N/A')
        high_target = ticker_info.get('targetHighPrice', 'N/A')

        # Financial Health
        total_debt = ticker_info.get('totalDebt', 'N/A')
        total_cash = ticker_info.get('totalCash', 'N/A')
        book_value = ticker_info.get('bookValue', 'N/A')
        operating_margins = ticker_info.get('operatingMargins', 'N/A')
        profit_margins = ticker_info.get('profitMargins', 'N/A')
        roe = ticker_info.get('returnOnEquity', 'N/A')
        revenue_growth = ticker_info.get('revenueGrowth', 'N/A')

        # Display Company Information
        try:
            st.markdown("---")
            st.subheader(f"Company: {name}")
            st.write("**Business Summary:**")
            st.write(summary if summary != 'N/A' else "No summary available")
            st.markdown(f'[Company Website]({website})' if website != 'N/A' else "No website available")
            st.markdown("<hr><br>", unsafe_allow_html=True)

            company_meta_data = {
                'Market Cap': [f'${market_cap:,}' if isinstance(market_cap, int) else "No data"],
                'Sector': [sector if sector != 'N/A' else "No data"],
                'Industry': [industry if industry != 'N/A' else "No data"],
                'Employees': [f'{full_time_employees:,}' if isinstance(full_time_employees, int) else "No data"],
                'Revenue/Employee': [f'${rev_per_employee:,}' if isinstance(rev_per_employee, (int, float)) else "No data"]
            }
            st.table(pd.DataFrame(company_meta_data))
        except Exception as e:
            st.write("Unable to display company information")

        # Prices Output
        try:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Prices 🏷")
                st.write(f"Current Price: ${current_price:,}" if current_price != 'N/A' else "Current Price: No data")
                st.write(f"52 Week Low: ${fiftytwo_low:,}" if fiftytwo_low != 'N/A' else "52 Week Low: No data")
                st.write(f"52 Week High: ${fiftytwo_high:,}" if fiftytwo_high != 'N/A' else "52 Week High: No data")
            with col2:
                st.subheader("Target Prices 🎯")
                st.write(f"Mean: ${mean_target}" if mean_target != 'N/A' else "Mean: No data")
                st.write(f"Low: ${low_target}" if low_target != 'N/A' else "Low: No data")
                st.write(f"High: ${high_target}" if high_target != 'N/A' else "High: No data")

            st.markdown(f"**Recommendation:** `{recomm_key}`" if recomm_key != 'N/A' else "**Recommendation:** No data")
            st.markdown("---")
        except Exception as e:
            st.write("Unable to display price information")

        # Charts
        try:
            ticker_df = ticker_data.history(period='1y')
            st.subheader("Stock Performance 📈")
            st.write("Historical Close Price")
            st.line_chart(ticker_df['Close'])
            st.write(f"Stock Volume")
            st.bar_chart(ticker_df['Volume'])
        except Exception as e:
            st.write("Unable to display stock performance charts")

        # Financial Health Output
        try:
            st.subheader("Financial Health 💰")

            total_debt = ticker_info.get('totalDebt', 0)
            total_cash = ticker_info.get('totalCash', 0)
            book_value = ticker_info.get('bookValue', 0)
            operating_margins = ticker_info.get('operatingMargins', 'N/A')
            profit_margins = ticker_info.get('profitMargins', 'N/A')
            roe = ticker_info.get('returnOnEquity', 'N/A')
            revenue_growth = ticker_info.get('revenueGrowth', 'N/A')

            total_debt = total_debt if isinstance(total_debt, (int, float)) else 0
            total_cash = total_cash if isinstance(total_cash, (int, float)) else 0
            book_value = book_value if isinstance(book_value, (int, float)) else 0

            st.write(f"Total Debt: ${total_debt:,}" if total_debt else "Total Debt: No data")
            st.write(f"Total Cash: ${total_cash:,}" if total_cash else "Total Cash: No data")
            st.write(f"Book Value: {book_value}" if book_value else "Book Value: No data")
            st.write(f"Operating Margins: {operating_margins}" if operating_margins != 'N/A' else "Operating Margins: No data")
            st.write(f"Profit Margins: {profit_margins}" if profit_margins != 'N/A' else "Profit Margins: No data")
            print(f"Roe: {roe}")
            st.write(f"Return on Equity (ROE): {roe}" if roe != 'N/A' else "Return on Equity (ROE): No data")
            st.write(f"Revenue Growth: {revenue_growth}" if revenue_growth != 'N/A' else "Revenue Growth: No data")

            st.markdown("<hr><br>", unsafe_allow_html=True)
        except Exception as e:
            st.write(f"Unable to display financial health information: {e}")



        
        # Income Statement, Balance Sheet, Cash Flow
        try:
            st.subheader("Financial Statements 📊")
            st.write("Income Statement")
            st.dataframe(ticker_data.income_stmt)
            st.write("Balance Sheet")
            st.dataframe(ticker_data.balance_sheet)
            st.write("Cash Flow")
            st.dataframe(ticker_data.cashflow)
            st.markdown("<hr><br>", unsafe_allow_html=True)
        except Exception as e:
            st.write("Unable to display financial statements")

        # Recommendations Output
        try:
            st.subheader("Street Recommendations 🏦")
            num_analyst_opinions = ticker_info.get('numberOfAnalystOpinions')
            avg_analyst_rating = ticker_info.get('averageAnalystRating')

            if num_analyst_opinions and avg_analyst_rating:
                st.write(f"Number of Analyst Opinions: {num_analyst_opinions}")
                st.write(f"Average Analyst Rating: {avg_analyst_rating} [Lower is better, with 1 = Strong Buy, 5 = Strong Sell]")
            else:
                st.write("No analyst recommendations available.")
            st.markdown("<hr><br>", unsafe_allow_html=True)
        except Exception as e:
            st.write("Unable to display analyst recommendations")

        # Major Holders
        try:
            holders = ticker_data.institutional_holders
            if holders is not None:
                st.subheader("Major Holders")
                st.dataframe(holders)
            else:
                st.write("No major holders data available.")
            st.markdown("<hr><br>", unsafe_allow_html=True)
        except Exception as e:
            st.write("Unable to display major holders information")
        
        # Company Risk
        try:
            st.subheader("Risk Assessment ⚠️")
            st.write("\nThe lower the number, the least amount of Risk\n")
            st.write(f"Audit Risk: {ticker_info.get('auditRisk', 'No data')}")
            st.write(f"Compensation Risk: {ticker_info.get('compensationRisk', 'No data')}")
            st.write(f"Shareholder Risk: {ticker_info.get('shareHolderRightsRisk', 'No data')}")
            st.write(f"Overall Risk: {ticker_info.get('overallRisk', 'No data')}")
            st.markdown("<hr><br>", unsafe_allow_html=True)
        except Exception as e:
            st.write("Unable to display risk assessment information")

        # News Output
        try:
            st.subheader("Recent News 📰")
            num_stories = 10
            news = get_ticker_news(ticker, num_stories)
            if isinstance(news, dict):
                if 'stories' in news and len(news['stories']) > 0:
                    st.write(f"Displaying {len(news['stories'])} articles.")
                    for i, story in enumerate(news['stories']):
                        article_title = story.get('title', 'No Title')
                        article_link = story.get('url', '#')
                        st.markdown(f"{i + 1}. [{article_title}]({article_link})")
                else:
                    st.write("No articles found.")
            else:
                st.write("Unable to fetch news articles.")
        except Exception as e:
            st.write("Unable to display news information")

    except Exception as e:
        st.error(f"An error occurred: {e}")
