import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

@st.cache_data
def load_data():
    iries=load_iris()
    df=pd.DataFrame(iries.data,columns=iries.feature_names)
    df['species']=iries.target
    return df , iries.target_names

df,target_name= load_data()

model=RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])
st.sidebar.title("Input_features")
sepal_length=st.sidebar.slider("Sepal Length ", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width=st.sidebar.slider("Sepal Width ", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length=st.sidebar.slider("Petal Length ", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width=st.sidebar.slider("Petal Width ", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

input_data=[[sepal_length,sepal_width,petal_length,petal_width]]
# prediction
prediction=model.predict(input_data)
predicted_species=target_name[prediction[0]]

st.write("Prediction")
st.write(f'The predicted specie is {predicted_species}')