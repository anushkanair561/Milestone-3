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
message = "##### Do you want to discover new places just for you? Click below!"
st.write(message)
st.link_button("Parks & Rec in San Jose", "https://www.yelp.com/search?find_desc=Parks+And+Recreation&find_loc=San+Jose%2C+CA")


st.divider()
message = "#### Watch the video below to learn some tips to keep in mind when planning your visit"
st.write(message)
VIDEO_URL = "https://www.youtube.com/watch?v=60V7n3nKxvI"
st.video(VIDEO_URL)

st.subheader('Additional Assisant Features', divider='grey')
col1, col2, col3 = st.columns(3)
with col1:
   st.page_link("main_page.py", label="Welcome", disabled=True)

with col2:
   st.page_link("pages/assistant_st.py", label="Assistant")

with col3:
   st.page_link("pages/vision.py", label="Vision")

