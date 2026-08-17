from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq

load_dotenv(find_dotenv())


llm = ChatGroq(
    model = 'qwen/qwen3.6-27b',
    temperature=0.1,
    reasoning_format="hidden"
)
