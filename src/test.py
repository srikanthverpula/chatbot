
import json
import openai
import app
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

def sample(user_query,chat_histories):

    try:
        print(user_query,chat_histories)
        template = """
        You are a helpful assistant. Answer the following questions considering the history of conversation:
        Chat history: {chat_histories}
        User question: {user_query}
        """
        prompt = ChatPromptTemplate.from_template(template)

        # Create a pipeline using the ChatOpenAI module and StrOutputParser
        chain = prompt | ChatOpenAI() | StrOutputParser()

        # Build the prompt with user query and chat history
        built_prompt = chain.build_prompt({
            "chat_histories": chat_histories,
            "user_query": user_query
        })

        # Specify the OpenAI model and generate completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            prompt=built_prompt,
        )
        response_message = response["choices"][0]["message"]
        return response_message

    except Exception as e:
        # Log the error message or handle it as per your requirement
        print("Error occurred:", e)
        return None