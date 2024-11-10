import streamlit as st
import pandas as pd
import numpy as np
import time

st.markdown("## Welcome to the Parks & Recreational Center Assistant!")
st.sidebar.markdown("# Welcome Page")

message = "#### If you are someone who enjoys the outdoors and is located in San Jose, I can help! "
st.write(message)

st.image("https://sanjosespotlight.s3.us-east-2.amazonaws.com/wp-content/uploads/2022/07/28102515/DSC_0610-4-1160x560.jpg")

st.divider()

message = "#### Do you want to discover new places just for you? Click below!"
st.write(message)
st.link_button("Parks & Rec in San Jose", "https://www.yelp.com/search?find_desc=Parks+And+Recreation&find_loc=San+Jose%2C+CA")
st.divider()

st.markdown("### San Jose Park Video")

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

st.divider()

st.subheader('Additional Assisant Features', divider='grey')
col1, col2, col3 = st.columns(3)
with col1:
   st.page_link("main_page.py", label="Welcome", disabled=True)

with col2:
   st.page_link("pages/assistant_st.py", label="Assistant")

with col3:
   st.page_link("pages/vision.py", label="Vision")

