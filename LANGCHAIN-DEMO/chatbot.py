from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenRouter(
    model=os.getenv("MODEL")
)
# this is the way to store the conversation history in a list so that the chatbot can remember the previous conversations and respond accordingly
conversation_history=[]

while True:
    user_input = input("You: ")
    #this is allowing the chatbot to remember the conversation history and respond accordingly
    conversation_history.append(user_input)
    if user_input.lower()=="exit":
        break
    response = model.invoke(conversation_history)
    conversation_history.append(response.content)
    print(response.content)

print(conversation_history)