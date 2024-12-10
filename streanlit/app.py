import streamlit as st
import pandas as pd
import numpy as np


st.title("Hello ! , My name Is Khushi Rajpurohit")

st.write("I am a Data Scientist")

df=pd.DataFrame({
    'name':["khushi",'Monal'],
    'JOB':['Data Scientist','DATA Engineer']
})

st.write(df)

line_chart=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])

st.line_chart(line_chart)