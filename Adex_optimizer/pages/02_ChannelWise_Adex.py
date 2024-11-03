import streamlit as st
import pandas as pd
import numpy as np
import time
import openpyxl

st.set_page_config(page_title="ChannelWise Adex",
                   page_icon="image.png", layout="wide")

with open("Adex_optimizer/style.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.markdown("# Channel wise Adex Data",
            unsafe_allow_html=True)
st.markdown('---')


def channel_list(df):
    channel_list = set(df.Channel)
    channel_list_final = []
    for s in channel_list:
        channel_list_final.append(s)
    return channel_list_final


def month_list(df):
    month_list = set(df.Month)
    month_list_final = []
    for s in month_list:
        month_list_final.append(s)
    return month_list_final


def region_list(df):
    region_list = set(df.Region)
    region_list_final = []
    for s in region_list:
        region_list_final.append(s)
    return region_list_final


def channel_wise_adex(df, channel):
    criteria1 = df.Channel == channel
    select_df_name = df.loc[criteria1, :]
    return select_df_name


def secondage_analysis_channel(df_channel):
    channel_level_analysis = (round(df_channel.describe().Total_Seconds))
    return channel_level_analysis


try:
    adex_afterdrop = st.session_state.adex_after_drop
    channel_options = channel_list(adex_afterdrop)
    if channel_options not in st.session_state:
        st.session_state["channel_options"] = channel_options
    with st.sidebar:
        st.markdown("## Select Channel Option")
        st.markdown("---")
        channel_select = st.selectbox(
            label="Channel Selection", options=channel_options, key="channel_select")
        rate_input = st.number_input(label="Input Rates", value=0, step=10,
                                     key="Input  Rates", placeholder="Type Average Channel ER")

    st.subheader(channel_select)
    st.markdown("---")
    st.dataframe(channel_wise_adex(adex_afterdrop, channel=channel_select))

    df_channel = channel_wise_adex(adex_afterdrop, channel=channel_select)
    st.subheader("Channel Level Ad Seconds Analysis")
    st.markdown("---")
    col1, col2 = st.columns(2)

    col1.number_input(label="Total Seconds",
                      value=df_channel.Total_Seconds.sum(), key="Input seconds")
    col2.number_input(label="Total Revenue Estimation", value=round(
        (df_channel.Total_Seconds.sum()*rate_input)/10), key="Input_value")
    st.markdown("---")
    col4, col5, col6 = st.columns(3)
    col4.number_input(label="Mean Secondage", value=round(
        df_channel.Total_Seconds.mean()), key="Input mean")
    col5.number_input(label="Advertiser Count", value=round(
        df_channel.Total_Seconds.count()), key="Input count")
    col6.number_input(label="Max Consumption Levels", value=round(
        df_channel.Total_Seconds.max()), key="Input max")
    if df_channel not in st.session_state:
        st.session_state["df_channel"] = df_channel
except:
    if NameError:
        pass
    if ValueError:
        pass
    if AttributeError:
        pass
