import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
import helper

load_dotenv()

st.title("Sample ChatBot")

# Initialize chat history list in session state if not present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)

# User input with unique key
user_query = st.text_input("Your message", key="user_input")

# If user submits a query
if st.button("Send"):
    # Append user message to chat history
    if user_query:
        try:
            # Append HumanMessage to chat history
            human_message = HumanMessage(user_query)
            st.session_state.chat_history.append(human_message)
            
            # Display user message
            with st.chat_message("Human"):
                st.markdown(user_query)
            
            # Get AI response
            ai_response = helper.get_answer(user_query, st.session_state.chat_history)
            
            # Append AIMessage to chat history
            ai_message = AIMessage(ai_response)
            st.session_state.chat_history.append(ai_message)
            
            # Display AI response
            with st.chat_message("AI"):
                st.markdown(ai_response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
