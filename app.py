import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("My Cookie Dashboard!")

# st.subheader() is a smaller heading
st.subheader("An analysis of cookies")

# st.write() can display plain text or variables
st.write("This app is for all the cookie monsters.")


#CODE 1 
st.header("2. Widgets (User Inputs)")

# Text input box (default value = "Guest")
name = st.text_input("Enter your name:", "Guest")

# Slider (range: 0 to 100, default = 25)
age = st.slider("What is your age?", 0, 100, 25)

# Dropdown menu
favorite_cookie = st.selectbox("Your favorite cookie:", ["Chocolate chip", "Snickerdoodle", "Sprinkle", "Smore", "Double Chocolate", "Sugar",  "Oatmeal Raisin"])

# Display user inputs dynamically
st.write(f"Hello **{name}**! You are {age} years old and your favorite type of cookies are {favorite_cookie}!")

#CODE 2

# Initialize counter if it doesn't exist yet
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Button to increment counter
st.write(f"Hello **{name}**! You have {st.session_state.counter} {favorite_cookie} Cookies!")
if st.button("Add a cookie :D"):
    st.session_state.counter += 1

# Display current counter value
st.write("Your cookies:", st.session_state.counter)

#REGRESSION PLOT

st.header("Regression Image")

st.image("CookieRegressionAnalysis.png", caption="Cookie Regression Plot")