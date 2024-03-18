# pip install streamlit langchain lanchain-openai python-dotenv

import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import helper



load_dotenv()

st.title("Sample ChatBot")
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]
for message in st.session_state.chat_history:
    if isinstance(message,HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    else:     
       with st.chat_message("AI"):
            st.markdown(message.content)    

user_query=st.chat_input("Your message")
chat_histories=st.session_state.chat_history
if user_query is not None and user_query !="":
    st.session_state.chat_history.append(HumanMessage(user_query))
    
    with st.chat_message("Human"):
        st.markdown(user_query)
    with st.chat_message("AI"):
        #ai_response=get_response(user_query,st.session_state.chat_history)
        ai_response=helper.get_answer(user_query,st.session_state.chat_history)
        #ai_response=dummy.get_response(user_query,st.session_state.chat_history)
        st.markdown(ai_response)    
        st.session_state.chat_history.append(AIMessage(ai_response))