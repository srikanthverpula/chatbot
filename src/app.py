import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import helper
import dummy

load_dotenv()
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

user_query = st.chat_input("Your message")
chat_histories = st.session_state.chat_history

if user_query is not None and user_query != "":
    st.session_state.chat_history = st.session_state.chat_history + [HumanMessage(user_query)]

    with st.chat_message("Human"):
        st.markdown(user_query)
    with st.chat_message("AI"):
        with st.spinner("Thinking..."):
            ai_response = helper.get_answer(user_query, st.session_state.chat_history)
            st.markdown(ai_response)
            st.session_state.chat_history = st.session_state.chat_history + [AIMessage(ai_response)]

# Display chat history
st.markdown("## Chat History")
for i, message in enumerate(st.session_state.chat_history, start=1):
    st.write(f"{i}. {message}")
    print(message)
