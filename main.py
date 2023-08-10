import streamlit as st
import plotly.express as px


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select number of forecast days ")
data = st.selectbox("Select data to view", options=("Sky", "Temperature"))

st.subheader(f"{data} for the next {days} days in {place}")

figure = px.line(x=date, y, )
st.plotly_chart(figure)


