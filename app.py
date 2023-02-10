
import streamlit as st
import json
import requests

st.set_page_config(page_title='Aditya Mote',page_icon=':alien:',layout='wide')
st.image("html.png")
st.header("Atleast someone tap on my link :)")
st.code("Hi Myself Aditya Mote")

st.write("This is my first time creating web :no_mouth: I created this with Streamlit python based-library which is used for Data Science & Machine Learning.")
st.write("Open Source is the Future :heart:")
st.markdown("In this website i will use an API if you tap on below button you will get the Surprise!")

response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
res = response.json()
insult = res["insult"]

if (st.button("Tap Here")):
   st.write(insult)

link = '[Github](https://github.com/Rx-Metallica) [Twitter](https://twitter.com/_Aditya_Mote_?s=09) [Instagram](https://instagram.com/____aditya_mote____?igshid=ZDdkNTZiNTM=)'

st.markdown(link,unsafe_allow_html=True)

hide_streamlit_style = """ <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
