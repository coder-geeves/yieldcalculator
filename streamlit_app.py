import streamlit as st

rpm = st.number_input("Rent Per Month", 0, 10000, 1000, 10) 
propVal = st.number_input("Property Value", 100000, 3000000, 250000, 5000)

st.write(f'{rpm * 12 / propVal:.2%}')
