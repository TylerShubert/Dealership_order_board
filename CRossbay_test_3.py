from click import option
import streamlit as st



import pandas as pd
from pathlib import Path

st.write("# CROSSBAY MOTORSPORTS")

st.write("# Hi, this is our first web app in Python! :sunglasses:")

KAWASAKI_CSV = pd.read_csv(
    Path("KAWA_SAMPLE_CSV.CSV"),
    infer_datetime_format=False)
df = pd.DataFrame(KAWASAKI_CSV)

KAWI_JET_SKI = pd.read_csv(
    Path("Jet_ski_samp.csv"),
    infer_datetime_format=False
)
Jet_DF = pd.DataFrame(KAWI_JET_SKI)


st.write("Dealer Price list")
price_list = st.image("KAWI_PIC_TEST_1.PNG")




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
st.write("Order Board")
if st.button("Kawasaki Street Bike"):
     st.write(df)
if st.button("Kawasaki Jet Ski"):
    st.write(Jet_DF)    