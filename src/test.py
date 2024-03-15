
import openai
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
def sample(user_query,chat_histories):

    try:
        print(user_query,chat_histories)
        template = """
        You are a helpful assistant. Answer the following questions considering the history of conversation:
        Chat history: {chat_histories}
        User question: {user_query}
        """
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | ChatOpenAI() | StrOutputParser()

        built_prompt = chain.build_prompt({
            "chat_histories": chat_histories,
            "user_query": user_query
        })

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            prompt=built_prompt,
        )
        response_message = response["choices"][0]["message"]
        return response_message

    except Exception as e:

        return f"Error occurred:{e}"