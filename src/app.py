import streamlit as st
from langchain_core.messages import HumanMessage
import helper

st.title("Sample ChatBot")

# Initialize chat history if not already present in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        st.write("Human:", message.content)
    else:
        st.write("AI:", message)  # Adjusted to handle both strings and objects

# User input
user_query = st.text_input("Your message")

# If user submits a query
if st.button("Send"):
    # Append user message to chat history
    if user_query:
        st.session_state.chat_history.append(HumanMessage(user_query))
        
        # Get AI response
        ai_response = helper.get_answer(user_query, st.session_state.chat_history)
        st.session_state.chat_history.append(ai_response)
        
        # Display AI response
        if isinstance(ai_response, str):
            st.write("AI:", ai_response)
        else:
            st.write("AI:", ai_response.content)
