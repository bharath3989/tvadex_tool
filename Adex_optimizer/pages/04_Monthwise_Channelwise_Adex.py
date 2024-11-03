import streamlit as st
import pandas as pd
import numpy as np
import time
import openpyxl


st.set_page_config(page_title="Monthwise-Regionwise Adex",
                   page_icon="image.png", layout="wide")

with open("/Users/bharathviswanathan/Desktop/Adex_optimizer/style.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.markdown("# Monthwise - Channel Level Adex Data",
            unsafe_allow_html=True)
st.markdown('---')

# list of user defined functions


def channel_list(df):
    channel_list = set(df.Channel)
    channel_list_final = []
    for s in channel_list:
        channel_list_final.append(s)
    return channel_list_final


def month_list(df):
    df.reset_index(inplace=True)
    month_list = set(df.Month)
    month_list_final = []
    for m in month_list:
        month_list_final.append(m)
    return month_list_final


def region_list(df):
    df.reset_index(inplace=True)
    region_list = set(df.Region)
    region_list_final = []
    for r in region_list:
        region_list_final.append(r)
    return region_list_final


def ascertain_channel_share(df):
    channel_share_data = df.groupby(["Month", "Channel"]).sum("Total_Seconds")
    return channel_share_data


def ascertain_regionwise_channel_share(df):
    regionwise_channel_share_data = df.groupby(
        ["Month", "Region", "Channel"]).sum("Total_Seconds")
    return regionwise_channel_share_data


def time_wise_adex(df, time):
    criteria1 = df.Month == time
    select_df_name = df.loc[criteria1, :]
    return select_df_name


def region_wise_adex(df, region):
    criteria1 = df.Region == region
    select_df_name = df.loc[criteria1, :]
    return select_df_name


def monthandtime_wise_adex(df, time, region):
    criteria1 = df.Month == time
    criteria2 = df.Region == region
    select_df_name = df.loc[(criteria1 & criteria2), :]
    return select_df_name


try:
    adex_afterdrop = st.session_state.adex_after_drop
    regional_share_df = ascertain_regionwise_channel_share(adex_afterdrop)
    region_list_final = region_list(regional_share_df)
    if region_list_final not in st.session_state:
        st.session_state["region_list_final"] = region_list_final
    channel_share_df = ascertain_channel_share(adex_afterdrop)
    month_list_final = month_list(channel_share_df)
    if month_list_final not in st.session_state:
        st.session_state["month_list_final"] = month_list_final

    with st.sidebar:
        st.markdown("## Select Region Option")
        st.markdown("---")
        region_select = st.selectbox(
            label="Region Selection", options=region_list_final, key="region_select")
        st.markdown("## Select Month Option")
        st.markdown("---")
        month_select = st.selectbox(
            label="Month Selection", options=month_list_final, key="month_select")
    col1, col2 = st.columns(2)
    col1.subheader("Monthwise Grouped Adex")
    col1.markdown("---")
    col1.dataframe(ascertain_channel_share(adex_afterdrop))
    col2.subheader("Filtered Monthwise Custom Adex")
    col2.markdown("---")
    time_wise_adex_split = time_wise_adex(
        df=channel_share_df, time=month_select)
    col2.dataframe(time_wise_adex_split)

    st.markdown("# Regionwise - Channel Level Adex Data",
                unsafe_allow_html=True)
    st.markdown('---')
    col3, col4 = st.columns(2)
    col3.subheader("Regionwise Grouped Adex")
    col3.markdown("---")
    col3.dataframe(ascertain_regionwise_channel_share(adex_afterdrop))
    col4.subheader("Filtered Regionwise Custom Adex")
    col4.markdown("---")
    region_wise_adex_Split = region_wise_adex(
        df=regional_share_df, region=region_select)
    col4.dataframe(region_wise_adex_Split)

    region_time_wise_splitdf = monthandtime_wise_adex(
        df=region_wise_adex_Split, region=region_select, time=month_select)
    st.subheader("Regionwise - Time Custom Grouped Adex")
    st.markdown("---")
    st.dataframe(region_time_wise_splitdf)

except:
    if NameError:
        pass
    if ValueError:
        pass
    if AttributeError:
        pass
