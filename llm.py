from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq

load_dotenv(find_dotenv())


llm = ChatGroq(model = 'llama-3.3-70b-versatile', temperature=0.1)
