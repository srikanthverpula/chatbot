import streamlit as st
from dotenv import load_dotenv
import helper

load_dotenv()

st.title("Sample ChatBot")

# Initialize chat history list
chat_history = []

# Display chat history
for message in chat_history:
    st.write("User:", message)

# User input
user_query = st.text_input("Your message")

# If user submits a query
if st.button("Send"):
    # Append user message to chat history
    if user_query:
        chat_history.append(user_query)
        
        # Get AI response
        ai_response = helper.get_answer(user_query, chat_history)
        chat_history.append(ai_response)
        
        # Display AI response
        st.write("AI:", ai_response)
