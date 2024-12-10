import streamlit as st
import pandas as pd 

st.title("Let me show you some widgets")

name=st.text_input("Enter your name ")
job= st.text_input("Enetr your job")
age=st.slider("select your age",0,100,25)
options=['Python','Java','C','C++']
choice=st.selectbox("Choice your fav computer language",options)
st.write(f'Fav Lang : {choice}')
if name:
    st.write(f'Name : {name}')

if job :
    st.write(f'Job: {job}')

if age:
    st.write(f'Name : {age}')

uploaded_file=st.file_uploader("chose a csv file",type='csv')
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)