import nltk
import streamlit as st
from afinn import Afinn

# Initialize the AFINN sentiment analyzer
afinn = Afinn()

def senti(text):
    result = afinn.score(text)
    if result > 0.05:
        st.header('Happy 😀')
    elif result < -0.05:
        st.header('Sad 😡')
    elif result >= -0.05 and result <= 0.05:
        st.header('No Emotion 😐')
    
st.header('Sentiment Analysis by Afinn')
text = st.text_area('Please Enter your message')
if st.button('Submit'):
    senti(text)