from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenRouter(
    model=os.getenv("MODEL")
)
# this is a simple example of how to use the ChatOpenRouter model to get a response to a question.
#  You can replace the question with any other question you want to ask.
response = model.invoke("What is the capital of India?")

print(response.content)