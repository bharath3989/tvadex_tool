import streamlit as st
import pandas as pd
import numpy as np
import time
import openpyxl


st.set_page_config(page_title="Consolidated Adex",
                   page_icon="image.png", layout="wide")

with open("/Users/bharathviswanathan/Desktop/Adex_optimizer/style.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.markdown("# Consolidated Adex",
            unsafe_allow_html=True)
st.markdown('---')


def consildated_adex(df):
    consolidated_adex = df.groupby(
        ["Advertiser", "Region", "Channel"]).sum("Total_Seconds")
    return consolidated_adex.unstack()


try:
    adex_afterdrop = st.session_state.adex_after_drop
    st.dataframe(consildated_adex(adex_afterdrop))

except:
    if NameError:
        pass
    if ValueError:
        pass
    if AttributeError:
        pass
