import streamlit as st
import pandas as pd
import numpy as np

st.title(':alien: Alien Sustainable Living')

with st.form(key='my_form'):

    st.header("Registration Form")
    name = st.text_input("Alien Name")
    eyes = st.number_input("Number of Eyes", min_value=0, max_value=10, step=1)
    planet = st.text_input("Home Planet")
    email = st.text_input("Email address (for Earth contact)")

    st.header("Alien Daily Life Survey")
    transport = st.selectbox("Main Mode of Interstellar Transportation", ["Solar Sail", "Wormhole", "Teleportation", "Other"])
    st.number_input("How many hours of the Earth day do you spend photosynthesizing?", min_value=0, max_value=24, step=1)
    st.number_input("How many Earth kilograms of waste does your household produce in a week?")
    st.number_input("What proportion of this is composted/recycled?")
    st.number_input("How many liters of water do you use in a day?")
    st.selectbox("How do you heat your home on cold space nights?", ["Geothermal Energy", "Burning Meteorites", "Other"])

    st.header("Sustainable Habits Commitment Form")
    st.number_input("I pledge to reduce my interstellar travel by (blank)% this solar cycle.", min_value=0, max_value=100, step=1)
    st.number_input("I pledge to compost/recycle (blank)% of my household waste by the next Martian summer.", min_value=0, max_value=100, step=1)
    st.number_input("I pledge to reduce my water usage by (blank)% by the time Halley's Comet next passes Earth.", min_value=0, max_value=100, step=1)
    st.selectbox("I pledge to convert my home heating to ... by the end of this lunar year.", ["Geothermal Energy", "Solar Energy", "Meteorite Burning", "Other"])

    st.header("Feedback Form")
    st.text_input("What part of our Alien Sustainable Living initiative have you enjoyed the most?")
    st.text_input("How could we improve our communication about green and sustainable initiatives?")
    st.text_area("Would you recommend our Alien Sustainable Living program to other extraterrestrial beings?")
    st.text_area("Any other suggestions for fun, green activities that our community should try?")

    st.form_submit_button('Confirm')

st.divider()

st.header("Some of your answers")
st.write("Name: ", name)
st.write("Eyes: ", int(eyes))
st.write("Planet: ", planet)
st.write("Email: ", email)
st.write("Transport: ", transport)
