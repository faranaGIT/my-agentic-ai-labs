from langchain_openrouter import ChatOpenRouter
# this will allow to separate the messages into different types like HumanMessage, AIMessage, SystemMessage
#  which will help to maintain the conversation history in a structured way.
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenRouter(
    model=os.getenv("MODEL")
)
# here we are initializing the conversation history with a SystemMessage that sets the context for the chatbot's behavior. This message will guide the chatbot to respond in a helpful,
#  humorous, and friendly manner while maintaining a professional tone.
# system message contains the persona, guardrails, and , and how the task should be handled.
#  Not the actual task as this is given my user. 
conversation_history=[
    SystemMessage(content="""
    You are a helpful AI assistant who answers queries with a bit of humour. Use emojis to make your response looks attractive. Give friendly answers while maintaining the professional tone.
    """)
]

while True:
    user_input = input("You: ")
    conversation_history.append(HumanMessage(content=user_input))
    if user_input.lower()=="exit":
        break
    response = model.invoke(conversation_history)
    conversation_history.append(AIMessage(content=response.content))
    print(response.content)

print(conversation_history)