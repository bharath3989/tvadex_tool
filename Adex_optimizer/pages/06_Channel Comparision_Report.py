import streamlit as st
import pandas as pd
import numpy as np
import time
import openpyxl

st.set_page_config(page_title="Channel Comparision Report",
                   page_icon="image.png", layout="wide")

with open("Adex_optimizer/style.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.markdown("# Channelwise Comparision Data",
            unsafe_allow_html=True)
st.markdown('---')

# list of user defined functions


def channel_level_advcompare(df, channel1, channel2, sfx1, sfx2):
    other_grouping_df_gbo = df.groupby(
        by=["Month", "Advertiser", "Brand", "Channel", "Region"])[["Total_Seconds"]].sum()
    other_grouping_df_gbo.reset_index(inplace=True)
    channel1_df_new = other_grouping_df_gbo[other_grouping_df_gbo.Channel == channel1]
    channel2_df_new = other_grouping_df_gbo[other_grouping_df_gbo.Channel == channel2]
    exclusive_df_pivot = pd.merge(left=channel1_df_new, right=channel2_df_new, how="outer", on=[
                                  "Month", "Region", "Advertiser", "Brand"], indicator=True, suffixes=(sfx1, sfx2))
    channel1_name = channel1+" " + "exclusive"
    channel2_name = channel2+" " + "exclusive"
    exclusive_df_pivot["_merge"] = exclusive_df_pivot._merge.cat.rename_categories(
        {'left_only': channel1_name, 'right_only': channel2_name, 'both': "Non Exclusive"})
    return exclusive_df_pivot


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
        st.markdown("## Select Options")
        st.markdown("---")

        channel1_select = st.selectbox(
            label="Channel1 Selection", options=channel_options, key="channel1_select")

        channel1_text = st.text_input(
            label="suffix_1", placeholder="Enter Suffix for channel1", key="suffix1")

        channel12_select = st.selectbox(
            label="Channel2 Selection", options=channel_options, key="channel2_select")

        channel2_text = st.text_input(
            label="suffix_2", placeholder="Enter Suffix for channel2", key="suffix2")

        region_select = st.selectbox(
            label="Region Selection", options=region_list_final, key="region_select")

        month_select = st.selectbox(
            label="Month Selection", options=month_list_final, key="month_select")

    channel_compare_df = channel_level_advcompare(
        df=adex_afterdrop, channel1=channel1_select, channel2=channel12_select, sfx1=channel1_text, sfx2=channel2_text)
    time.sleep(5)
    st.dataframe(channel_compare_df)
    channel1_name = channel1_select+" " + "exclusive"
    channel2_name = channel12_select+" " + "exclusive"

    channel1_select = channel_compare_df["_merge"] == channel1_name
    channel2_select = channel_compare_df["_merge"] == channel2_name

    channel1_exclusive = channel_compare_df.loc[channel1_select, :]
    channel2_exclusive = channel_compare_df.loc[channel2_select, :]

    st.subheader("Channel Level Ad Seconds Analysis")
    st.markdown("---")
    col1, col2 = st.columns(2)

    ch1_seconds = col1.number_input(label="Total Exclucive Seconds of channel1",
                                    value=round(channel1_exclusive.iloc[:, 5].sum()), key="Input seconds")
    rate_input_channel1 = col1.number_input(label="Input Avg ER For Channel 1", value=0, step=10,
                                            key="Input  Rates_1", placeholder="Type Average Channel ER for Channel 1")
    col1.number_input(label="Value of Exclusives Channel 1", value=round((ch1_seconds*rate_input_channel1)/10), step=0,
                      key="Input value_1")

    ch2_seconds = col2.number_input(label="Total Exclucive Seconds of channel2", value=round(
        (channel2_exclusive.iloc[:, 7].sum())), key="Input_value")

    rate_input_channel2 = col2.number_input(label="Input Avg ER For Channel 2", value=0, step=10,
                                            key="Input  Rates_2", placeholder="Type Average Channel ER for Channel 2")

    col2.number_input(label="Value of Exclusives Channel 2", value=round((ch2_seconds*rate_input_channel2)/10), step=0,
                      key="Input value_2")

    st.markdown("---")
    st.markdown("## Channelwise Comparision Data - With Region & Time Filters",
                unsafe_allow_html=True)
    st.markdown('---')

    channel_select_region = channel_compare_df["Region"] == region_select
    channel_select_time = channel_compare_df["Month"] == month_select
    channel_compare_region_df = channel_compare_df.loc[(
        channel_select_region & channel_select_time), :]
    st.dataframe(channel_compare_region_df)

    channel1_exclusive = channel_compare_region_df.loc[channel1_select, :]
    channel2_exclusive = channel_compare_region_df.loc[channel2_select, :]

    st.subheader("Channel Level Filtered Data Analysis")
    st.markdown("---")

    col3, col4 = st.columns(2)

    ch1_seconds_filter = col3.number_input(label="Total Exclusive Seconds channel1 - After Filters",
                                           value=round(channel1_exclusive.iloc[:, 5].sum()), key="Input seconds_filter1")
    rate_input_channel1_filter = col3.number_input(label="Input Avg ER For Channel 1", value=0, step=10,
                                                   key="Input  Rates_1_filter", placeholder="Type Average Channel ER for Channel 1")
    col3.number_input(label="Value of Channel 1 After Filter", value=round((ch1_seconds_filter*rate_input_channel1_filter)/10), step=0,
                      key="Input value_1_filter")

    ch2_seconds_filter = col4.number_input(label="Total Exclusive Seconds channel2 - After Filters", value=round(
        channel2_exclusive.iloc[:, 7].sum()), key="Input seconds_filter2")
    rate_input_channel2_filter = col4.number_input(label="Input Avg ER For Channel 2", value=0, step=10,
                                                   key="Input  Rates_2_filter", placeholder="Type Average Channel ER for Channel 2")
    col4.number_input(label="Value of Channel 2 After Filter", value=round((ch2_seconds_filter * rate_input_channel2_filter)/10), step=0,
                      key="Input value_2_filter")


except:
    if NameError:
        pass
    if ValueError:
        pass
    if AttributeError:
        pass
