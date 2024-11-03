import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="User Instructions",
                   page_icon="image.png", layout="wide")

with open("/Users/bharathviswanathan/Desktop/Adex_optimizer/style.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)


st.markdown("# Adex Optimizer - User Instructions",
            unsafe_allow_html=True)

st.markdown('---')
st.write('''
The app is one of its kind data consolidation app for Television adex across any markets.The app has been coded in such a way that all necessary reporting details from a television adex has been hardcoded at the backend and hence its the first plug in play model for Television adex optimisation for Indian Television industry. The app segements across multiple pages which helps the user to ascertain the below with just a click of a button.
1. The user gets to have a complete view of the channel wise adex data along with expected revenues that the channel would have done during the reporting period. The report also gives other key metrics such as mean share, number of advertisers, top advertiser contribution and so on.
2. consolidated adex data is a one sheet that gives channel wise adex data during the reporting period.
3. Monthwise-channelwise adex page helps user to filter the adex data channelwise - monthwise - regionwise to ascertain channel level - monthly level - region specefic contribution to the adex.
4. Exclusive Campaigns - To ascertain channelwise - monthwise - regionwise exclusive campaigns. The user could assess the market value of the exclusives on the go through this app.
5. Channelwise Comparision is one of its kind reporting format to compare between any two channel in the market and ascertain the value of exclsuives between them.

 ''')

st.markdown(
    "## Pre Requiste for using the app")
st.markdown('---')
st.write(''' 
1. Adex output with below mentioned columns in .xlsx format
2. Sheet name of the excel file where the data resides

The excel sheet uploaded should have the below mentioned columns 

1. Market
2. Period
3. Year
4. FY
5. Region
6. Super Category
7. Product Group
8. Advertiser
9. Brands
10. Channel
11. Total
''')

st.write('''Once upload happens and sheet name filled The app automatically reworks on the backend on the data where in column names are altered and only required columns are kept on the data. All this happens in a split seconds and then the the user gets a message that Database ready for usage.
''')

st.write('''
All database can be exported as CSV file or taken printout or enlarged directly with the button provided above the dataframes for appropriate user actions.

###  So Try the app. Get your optimizations in razor speed and keep pace with televsion advertising data in split seconds.
''')
