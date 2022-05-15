import streamlit as st

text = st.text_input("Input your name", 'Jiyang')
st.write("Output", f"Hello {text}!")
