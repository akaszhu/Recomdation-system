import streamlit as st
from streamlit_webrtc import webrtc_streamer

lang=st.text_input("Language")

if lang:
    webrtc_streamer(key="Key", desired_playing_state=True)

btn=st.button("Recommend")
