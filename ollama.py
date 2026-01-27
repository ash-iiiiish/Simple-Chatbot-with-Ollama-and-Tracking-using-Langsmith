import streamlit as st
from dotenv import load_dotenv
from langchain_community.llms import Ollama

load_dotenv()

st.title("Google Gemma Chatbot")

input_text=st.text_input("Enter your Question: ")

model = Ollama(model='gemma3')

if input_text:
    response=model.invoke(input_text)
    st.write(response)

    