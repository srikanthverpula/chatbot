import os
import uuid
import openai
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import helper
import dummy

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
st.title("Sample ChatBot")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    else:
        with st.chat_message("AI"):
            st.markdown(message.content)

unique_key = str(uuid.uuid4())
user_query = st.chat_input("Your message",key=unique_key)
chat_histories = st.session_state.chat_history
print(user_query)
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(user_query))
    with st.chat_message("Human"):
        st.markdown(user_query)
    try:
        with st.spinner("Thinking..."):
            ai_response = helper.get_answer(user_query, st.session_state.chat_history)
        with st.chat_message("AI"):
            st.markdown(ai_response)
            st.session_state.chat_history.append(AIMessage(ai_response))
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.session_state.chat_history.append(HumanMessage("practitioner details"))
    with st.chat_message("Human"):
        st.markdown("practitioner details")
    try:
        with st.spinner("Thinking..."):
            ai_response = helper.get_answer("practitioner details", st.session_state.chat_history)
        with st.chat_message("AI"):
            st.markdown(ai_response)
            st.session_state.chat_history.append(AIMessage(ai_response))
    except Exception as e:
        st.error(f"An error occurred: {e}")
