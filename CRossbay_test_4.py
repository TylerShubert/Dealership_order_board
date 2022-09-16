from click import option
import streamlit as st
from st_aggrid import AgGrid


import pandas as pd
from pathlib import Path

st.write("# CROSSBAY MOTORSPORTS")

st.write("# Hi, this is our first web app in Python! :sunglasses:")

KAWASAKI_CSV = pd.read_excel(
    Path("2023.xlsx"),
    index_col=0)








df = pd.read_excel('2023.xlsx')

newDF = AgGrid(df, height= 1000, width= 2000)

filteredDF = df.dropna(axis=0, how='all')






st.dataframe(AgGrid(df))
#st.write(df, index_col=0)
st.write(filteredDF)
#infer_datetime_format=False

CSV = pd.read_csv('2023WRF.CSV',na_filter= False)

filCSV = CSV.dropna(axis=1, how='all')

st.dataframe(filCSV.fillna(''))


if st.button("UnfilteredCSV"):
    st.write(CSV)

if st.button("filterCSV"):
    st.write(filCSV)

if st.button('DF2'):
    st.dataframe(filCSV.fillna(''))

KAWI_JET_SKI = pd.read_csv(
    Path("Jet_ski_samp.csv"),
    infer_datetime_format=False
)
Jet_DF = pd.DataFrame(KAWI_JET_SKI)

Street_Bike_price_list = ("KAWI_PIC_TEST_1.PNG")
Dual_sport = ("KAWI_PIC_TEST_2.PNG")

#st.write("Dealer Price list")
#price_list = st.image("KAWI_PIC_TEST_1.PNG")
st.write("PRICE LIST")
if st.button("Kawasaki Street Bike Price List"):
     st.image(Street_Bike_price_list)
if st.button("Kawasaki Dual sport"):
    st.image(Dual_sport)


#Street_Bike = print(df)
#Jet_Ski = print(Jet_DF)
#st.write(df)
#st.write(Jet_DF)
#st.multiselect("Please select a powersports class",options= ["Street Bike", "Jet Ski"])

#for st.multiselect in options:
    #if options == "Street Bike":
        #st.write(df),
        #Street_Bike
    #if options == "Jet Ski":
        #st.write(Jet_DF),
        #Jet_Ski



#input_value = st.text_input("Enter a Message")
st.write("ORDER BOARD")
if st.button("Kawasaki Street Bike"):
     st.write(df)
if st.button("Kawasaki Jet Ski"):
    st.write(Jet_DF)    