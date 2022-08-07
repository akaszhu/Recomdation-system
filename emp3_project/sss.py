import streamlit as st
import webbrowser
st.image("download.jpg")
st.title("EMOTION BASED MUSIC RECOMMENDATION")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("Choose your preffered language")
lang = st.radio("", ['English', 'Tamil'])
st.write("Camera wil be open to capture your emotion")
st.image("music-kids-2155774.jpg")
st.write("Your emotion is captured as", emotion)
if lang=="English":
        if emotion=="sad":
                url= 'https://open.spotify.com/playlist/54rzwtQ13PUsfxEWIUM6Qi?si=6462bc9233a94bf2'
                webbrowser.open_new_tab(url)
        elif emotion=="happy":  
                url= 'https://open.spotify.com/playlist/6oiaekDeyik4HtC9h4CS0v?si=78da089abd32449c'
                webbrowser.open_new_tab(url)
elif lang=="Tamil":
        if emotion=="sad":
                url= 'https://open.spotify.com/playlist/54rzwtQ13PUsfxEWIUM6Qi?si=6462bc9233a94bf2'
                webbrowser.open_new_tab(url)
        elif emotion=="happy":  
                url= 'https://open.spotify.com/playlist/6oiaekDeyik4HtC9h4CS0v?si=78da089abd32449c'
                webbrowser.open_new_tab(url)

