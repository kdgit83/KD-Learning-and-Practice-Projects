import streamlit as st
import numpy as np
import pandas as pd

## Title of the application
st.title("Hello from Streamlit")

## Display a simple text
st.write("This is some simple text")

## Create a simple Dataframe
df = pd.DataFrame({
    'Col_1': [1,2,3,4],
    'Col_2': [10,20,30,40]
})

## Display the Dataframe
st.write("Here is the Dataframe:")
st.write(df)

## Create a Line Chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
