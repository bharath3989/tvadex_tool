import streamlit as st
import pandas as pd
import numpy as np
import time
import openpyxl

st.set_page_config(page_title="Adex Optimizer",
                   page_icon="image.png", layout="wide")

with open("Adex_optimizer/style.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)


st.markdown("# Television Adex Analysis Tool",
            unsafe_allow_html=True)

st.markdown('---')
st.markdown('''
<style>
.big-font {
    font-size:20px !important;
}
</style>

<span class="big-font">Fully automated Television Adex analysis tool.</span>
''', unsafe_allow_html=True)
st.markdown('---')


def file_upload_status():
    st.success("File successfully uploaded")


file_uploaded = st.file_uploader(label="Upload only Excel file",
                                 type=[".xlsx"],
                                 key="uploadexcel", on_change=file_upload_status)

sheet_name = st.text_input("Select Sheet Name", key="sheetname",
                           type="default", placeholder="Fill Sheet Name")
st.markdown('---')

try:
    if file_uploaded and sheet_name:
        raw_adex_data = pd.read_excel(io=file_uploaded, sheet_name=sheet_name,
                                      names=["Langauge", "Month", "Year", "FY", "Region", "Sector", "Category", "Advertiser",
                                             "Brand", "Channel", "Total_Seconds"], header=0)
    else:
        st.warning("File not uploaded or sheet name not filled...Check")
    cols_to_drop = ["Langauge", "Year", "FY"]
    adex_after_drop = raw_adex_data.drop(columns=cols_to_drop)
    adex_after_drop["Month"] = pd.to_datetime(
        adex_after_drop["Month"], format="dd-mm-yy")
    # Adding Progress of work
    progress_text = "Database Optimizations Update, Deletion and Updation of Requisite Columns And Additions Of Required Features...."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.markdown("## Adex Database is ready to use....",
                unsafe_allow_html=True)
    if raw_adex_data not in st.session_state:
        st.session_state["raw_adex_data"] = raw_adex_data
    if adex_after_drop not in st.session_state:
        st.session_state["adex_after_drop"] = adex_after_drop
except:
    if NameError:
        pass
    if ValueError:
        pass
    if AttributeError:
        pass
