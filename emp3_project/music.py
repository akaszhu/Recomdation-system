import streamlit as st
from streamlit_webrtc import webrtc_streamer
lang= st.text_input("Language")
singer = st.text_input("singer")

if lang and singer:
    webrtc_streamer(key="key")
btn=st.button("Recommend me songs")
