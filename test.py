 #Prices Output
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Prices 🏷")
        st.write("Current Price:  ${:,.2f}".format(currentPrice))
        st.write("52 Week Low:  ${:,.2f}".format(fiftytwoLow))
        st.write("52 Week High:  ${:,.2f}".format(fiftytwoHigh))
    with col2:
        st.subheader("Target Prices 🎯")
        st.write(f"Target Mean Price: ${meanTarget:,}")
        st.write(f"Target Low Price: ${lowTarget}")
        st.write(f"Target High Price: ${highTarget}")