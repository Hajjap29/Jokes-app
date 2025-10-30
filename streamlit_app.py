import streamlit as st
import requests

st.title("😂 Joke Bot")

st.write("Hey there! Would you like to hear a random joke?")

# Buttons instead of text input
col1, col2 = st.columns(2)
with col1:
    yes = st.button("Yes, tell me a joke!")
with col2:
    no = st.button("No, maybe later")

if yes:
    # Fetch a random joke
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        st.success(joke["setup"])
        st.write("😄 " + joke["punchline"])
    else:
        st.error("Oops! Couldn't fetch a joke right now.")
elif no:
    st.info("Alright! Have a nice day 😊")
