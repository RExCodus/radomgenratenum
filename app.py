import streamlit as st
import random

st.title("Random NUmber Generator")

a=random.randint(1,100)

 st.write(f"Random number is: {a}")
