import streamlit as st
import os
import pandas as pd
import numpy as np
import time

st.write("## Welcome to ParkPal!")
st.sidebar.markdown("# Welcome Page")

st.write("###### If you are someone who enjoys the outdoors and is located in San Jose, I can help! ")

st.image("park_pal_logo.png")
st.subheader( "", divider="orange")

st.write("### San Jose Park Video")

def park_video(option):
   if option == "Almaden Lake Park":
      VIDEO_URL = "https://www.youtube.com/watch?v=ASWa2HQvixY"
   elif option == "Alum Rock Park":
      VIDEO_URL = "https://www.youtube.com/watch?v=c7YqiWIxEF0"
   elif option == "Emma Prusch Farm Park":
      VIDEO_URL = "https://www.youtube.com/watch?v=zWckXvI8SWU"
   elif option == "Kelley Park":
      VIDEO_URL = "https://www.youtube.com/watch?v=XoxiwPgz_hc"
   elif option == "Lake Cunningham Park":
      VIDEO_URL = "https://www.youtube.com/watch?v=kj1z2R6pMfw"
   elif option == "Overfelt Gardens Park":
      VIDEO_URL = "https://www.youtube.com/watch?v=04bzBx4AfQc"
   else:
      return None
   
   return st.video(VIDEO_URL)

option = st.selectbox(
    "Choose a park below to see a video of it",
    ("Almaden Lake Park", "Alum Rock Park", "Emma Prusch Farm Park", "Kelley Park", "Lake Cunningham Park", "Overfelt Gardens Park"),
    index=None,
    placeholder="Select park",
)

park_video(option)
st.subheader("", divider='orange')

st.write("### Additional Assisant Features")

col1, col2, col3, col4 = st.columns(4)
with col1:
   st.page_link("Welcome.py", label="Welcome", disabled=True)

with col2:
   st.page_link("pages/Make_Reservation.py", label="Make Reservation")

with col3:
   st.page_link("pages/ParkPal_Chatbot.py", label="ParkPal Chatbot")

with col4:
   st.page_link("pages/Upload_Park_Sign.py", label="Upload Park Sign")

