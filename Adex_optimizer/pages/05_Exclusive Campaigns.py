import streamlit as st
import pandas as pd
import numpy as np
import time
import openpyxl

st.set_page_config(page_title="Exclusive Campaigns",
                   page_icon="image.png", layout="wide")

with open("Adex_optimizer/style.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.markdown("# Channelwise Exclusive Adex Data",
            unsafe_allow_html=True)
st.markdown('---')

# list of user defined functions


def dataframe_exclusivity(df, channel_name):
    other_grouping_df_gbo = df.groupby(
        by=["Month", "Advertiser", "Brand", "Channel", "Region"])[["Total_Seconds"]].sum()
    other_grouping_df_gbo.reset_index(inplace=True)
    channel_df_new = other_grouping_df_gbo[other_grouping_df_gbo.Channel == channel_name]
    return channel_df_new


def dataframe_exclusivity_filtered_region_time(df, channel_name, region, time):
    other_grouping_df_gbo = df.groupby(
        by=["Month", "Advertiser", "Brand", "Channel", "Region"])[["Total_Seconds"]].sum()
    other_grouping_df_gbo.reset_index(inplace=True)
    c1 = other_grouping_df_gbo.Channel == channel_name
    c2 = other_grouping_df_gbo.Region == region
    c3 = other_grouping_df_gbo.Month == time
    channel_df_new = other_grouping_df_gbo.loc[(c1 & c2 & c3), :]
    return channel_df_new


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


try:
    adex_afterdrop = st.session_state.adex_after_drop
    channel_options = st.session_state.channel_options
    region_list_final = st.session_state.region_list_final
    month_list_final = st.session_state.month_list_final

    with st.sidebar:
        st.markdown("## Select Channel Option")
        st.markdown("---")
        channel_select = st.selectbox(
            label="Channel Selection", options=channel_options, key="channel_select")
        st.markdown("## Select Region Option")
        st.markdown("---")
        region_select = st.selectbox(
            label="Region Selection", options=region_list_final, key="region_select")
        st.markdown("## Select Month Option")
        st.markdown("---")
        month_select = st.selectbox(
            label="Month Selection", options=month_list_final, key="month_select")
    exclusive_df = dataframe_exclusivity(
        df=adex_afterdrop, channel_name=channel_select)
    st.dataframe(exclusive_df)

    st.markdown("## Channel Exclusives - Filter",
                unsafe_allow_html=True)
    st.markdown('---')
    custom_exclusive_df_region_time = dataframe_exclusivity_filtered_region_time(
        df=adex_afterdrop, channel_name=channel_select, region=region_select, time=month_select)
    st.dataframe(custom_exclusive_df_region_time)

except:
    if NameError:
        pass
    if ValueError:
        pass
    if AttributeError:
        pass
