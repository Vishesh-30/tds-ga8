import pandas as pd
import numpy as np
import streamlit as st

st.header('Enter Values')
def user_input_features():
    First = st.number_input('Enter Second No.',min_value=0,max_value=2000000,step = 1)
    Second = st.number_input('Enter Second No.',min_value=0,max_value=1000000,step = 1)
    Third = st.number_input('Enter Third No.',min_value=0,max_value=900000,step = 1)
    Numbers = [First, Second, Third]
    return Numbers

list = user_input_features()
max = max(list)
st.write(list)
st.write('Maximum of three no is ')
st.write(max)
