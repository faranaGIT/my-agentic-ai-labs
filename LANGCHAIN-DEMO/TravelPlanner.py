from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import load_prompt
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenRouter(
    model=os.getenv("MODEL")
)
# this i loading the prompt template that we created in gereate_prompt.py. 
# This template will be used to generate a personalized travel itinerary based on the user's profile.
prompt = load_prompt('travel_planner_prompt.json')

chain = prompt | model | StrOutputParser() #LCEL

# print(chain.invoke({'username': 'Dhiraj', 'destination': 'Singapore', 'start_date':'25-01-2026', 'end_date':'30-01-2026','interests':'Adventure','travel_style':'Solo','dietary_preferences':'Non-Vegetarian', 'budget': '100000'}))

for chunk in chain.stream({'username': 'Dhiraj', 'destination': 'Singapore', 'start_date':'25-01-2026', 'end_date':'30-01-2026','interests':'Adventure','travel_style':'Solo','dietary_preferences':'Non-Vegetarian', 'budget': '100000'}):
    print(chunk, end="", flush=True)