import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")

st.title("In Search of Happiness")
x = st.selectbox("Select the data for X-axis", ("GDP", "Happiness", "Generosity"))
y = st.selectbox("Select the data for Y-axis", ("GDP", "Happiness", "Generosity"))


match x:
    case 'GDP':
        ex = df['gdp']
    case 'Happiness':
        ex = df['happiness']
    case 'Generosity':
        ex = df['generosity']

match y:
    case "GDP":
        ey = df['gdp']
    case "Happiness":
        ey = df['happiness']
    case "Generosity":
        ey = df['generosity']

st.subheader(f"{x} and {y}")
figure = px.scatter(x=ex, y=ey, labels={"x": x, "y": y})
st.plotly_chart(figure)