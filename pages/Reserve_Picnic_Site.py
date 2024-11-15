import streamlit as st
import os
import pandas as pd
import numpy as np
import time

# Display chat history
# Streamlit UI
st.write("## Make a Picnic Site Reservation")

st.image("https://www.ebparks.org/sites/default/files/styles/16x9_1000w/public/RO_GaryCrabbe-170423s_EBRPD-0303.jpg?h=c42ad62b&itok=Mq0juimf5")

st.subheader( "", divider="orange")

st.write("#### Select a park to access the Reservation Page:")

def park_video(option):
   if option == "Almaden Lake Park":
      SITE_URL = "https://anc.apm.activecommunities.com/sanjoseparksandrec/reservation/search?locale=en-US&reservationGroupIds=7"
   elif option == "Alum Rock Park":
      SITE_URL = "https://anc.apm.activecommunities.com/sanjoseparksandrec/reservation/search?locale=en-US&reservationGroupIds=5"
   elif option == "Emma Prusch Farm Park":
      SITE_URL = "https://anc.apm.activecommunities.com/sanjoseparksandrec/reservation/search?locale=en-US&reservationGroupIds=4"
   elif option == "Kelley Park":
      SITE_URL = "https://anc.apm.activecommunities.com/sanjoseparksandrec/reservation/search?locale=en-US&reservationGroupIds=2"
   elif option == "Lake Cunningham Park":
      SITE_URL = "https://anc.apm.activecommunities.com/sanjoseparksandrec/reservation/search?locale=en-US&reservationGroupIds=6"
   elif option == "Overfelt Gardens Park":
      SITE_URL = "https://anc.apm.activecommunities.com/sanjoseparksandrec/reservation/search?locale=en-US&reservationGroupIds=1"
   else:
      return None
   
   return st.link_button(option, SITE_URL)

option = st.selectbox(
    "Choose a park to access the reservation system and find a facility or site in that park that you can book for an available date and time.",
    ("Almaden Lake Park", "Alum Rock Park", "Emma Prusch Farm Park", "Kelley Park", "Lake Cunningham Park", "Overfelt Gardens Park"),
    index=None,
    placeholder="Select park",
)

park_video(option)
