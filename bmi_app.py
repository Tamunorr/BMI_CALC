import streamlit as st
from PIL import Image

st.header("BMI CHECKER")

w = st.number_input("Weight in Kilograms",step=0.1)
h = st.number_input("Height in meters")

def bmi_cal(w,h):
    bmi = w/(h**2)
    bmi = round(bmi)
    return(bmi)

def bmi_status(bmi):
    if bmi < 18.5:
        return "You are at risk of being underweight"
    elif 18.4 < bmi < 25:
        return "You are healthy"
    elif 24.9 < bmi < 30:
        return "You are at risk of being overweight"
    else:
        return "You are at risk of being obese"
    
if st.button("Calculate"):
    bmi = bmi_cal(w,h)
    status = bmi_status(bmi)

    st.write(f"Your BMI is {bmi}")
    st.write(status)