import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
import helper

load_dotenv()

st.title("Sample ChatBot")

# Initialize chat history list
chat_history = []

user_query = st.text_input("Your message")
if st.button("Send"):
    if user_query:
        # Append user message to chat history
        chat_history.append(HumanMessage(user_query))

        # Get AI response
        ai_response = helper.get_answer(user_query, chat_history)
        chat_history.append(ai_response)

        # Display AI response
        st.write("AI:", ai_response.content if isinstance(ai_response, AIMessage) else ai_response)
