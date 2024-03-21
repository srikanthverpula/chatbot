import streamlit as st
from dotenv import load_dotenv
import helper
from langchain_core.messages import HumanMessage,AIMessage

load_dotenv()
st.title("Sample ChatBot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]
for message in st.session_state.chat_history:
    print(message)
    print(isinstance(message,HumanMessage))
    if isinstance(message,HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    else:     
       with st.chat_message("AI"):
            st.markdown(message.content)    

user_query=st.chat_input("Your message")
chat_histories=st.session_state.chat_history
if user_query is not None and user_query !="":
    chat_user_query=user_query
    st.session_state.chat_history.append(HumanMessage(chat_user_query))
    
    with st.chat_message("Human"):
        st.markdown(user_query)
    with st.chat_message("AI"):
        with st.spinner("Thinking..."):
            ai_response=helper.get_answer(user_query,st.session_state.chat_history)
            st.markdown(ai_response)    
            st.session_state.chat_history.append(AIMessage(ai_response))
