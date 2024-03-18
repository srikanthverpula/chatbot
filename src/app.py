import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
import helper

load_dotenv()

st.title("Sample ChatBot")

# Initialize chat history list
chat_history = []

# Display chat history
for message in chat_history:
    if isinstance(message, HumanMessage):
        st.write("Human:", message.content)
    else:
        st.write("AI:", message.content)

# User input
user_query = st.text_input("Your message")

# If user submits a query
if st.button("Send"):
    # Append user message to chat history
    if user_query:
        chat_history.append(HumanMessage(str(user_query)))
        
        # Get AI response
        ai_response = helper.get_answer(user_query, chat_history)
        chat_history.append(ai_response)
        
        # Display AI response
        if isinstance(ai_response, AIMessage):
            st.write("AI:", ai_response.content)
        else:
            st.write("AI:", ai_response)
