from click import option
import streamlit as st
from st_aggrid import AgGrid


import pandas as pd
from pathlib import Path

st.write("# CROSSBAY MOTORSPORTS")

st.write("# Hi, this is our first web app in Python! :sunglasses:")


CSV = pd.read_csv('2023RC.CSV',na_filter= False)

filCSV = CSV.dropna(axis=1, how='all')

def color_coding(row):
    if row == 0,1 
    return ['background-color:red'] 
    
#else ['background-color:green'] * len(row)

st.dataframe(filCSV.style.apply(color_coding, axis=1))
#filCSV.style.highlight_min(axis=1)

if st.button('DF2'):
    st.dataframe(filCSV.fillna(''))

if st.button('DF3'):
    st.table(filCSV)


    





