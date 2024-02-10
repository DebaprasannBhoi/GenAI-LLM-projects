# Q&A Chatbot
from langchain.llms import OpenAI

#from dotenv import load_dotenv
import openai

# Set your API key here
openai.api_key = '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'

# Now you can use OpenAI API

#load_dotenv()  # take environment variables from .env.

import streamlit as st
import os


## Function to load OpenAI model and get respones

def get_openai_response(question):
    llm=OpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0.5)
    response=llm(question)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)




