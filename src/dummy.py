from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate

from langchain.schema import AIMessage,HumanMessage,SystemMessage
load_dotenv()

def get_response(user_query, chat_history):
    """
    Get AI response based on user query and chat history.

    Args:
        user_query (str): The user's query.
        chat_history (list): List of chat messages.

    Returns:
        str: AI response to the user query.
    """
    try:
        openai_chat_instance = ChatOpenAI(temperature=0, model='gpt-3.5-turbo')
        if not isinstance(chat_history, list):
            raise ValueError("chat_history must be a list of messages")

        chat_history_str = ' '.join(str(message.content) for message in chat_history)

        system_message = SystemMessage(content=f"You are a helpful assistant. You have to check responses from {chat_history_str} before going anywhere. If you find a response, you should send this only.")
        messages = [system_message, HumanMessage(content=user_query)]

        ai_response = openai_chat_instance(messages=messages).content

        return ai_response
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None