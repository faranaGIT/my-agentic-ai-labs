from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import load_prompt
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

model = ChatOpenRouter(
    model=os.getenv("MODEL")
)

st.header('Travel Planner')

username = st.text_input("Name")
destination = st.text_input("Destination")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")
budget = st.slider("Select Budget", 10000, 1000000)
interest = st.multiselect("Interests", ["Adventure", "Beaches", "Nature", "Shopping"])
travel_style = st.multiselect("Travel Style", ["Luxury", "Solo", "Group", "Family"])
dietary_preferences = st.selectbox("Dietary Preferences", ["Vegetarian", "Non-Vegetarian", "Vegan"])

prompt = load_prompt('travel_planner_prompt.json')

chain = prompt | model | StrOutputParser() #LCEL

# print(chain.invoke({'username': 'Dhiraj', 'destination': 'Singapore', 'start_date':'25-01-2026', 'end_date':'30-01-2026','interests':'Adventure','travel_style':'Solo','dietary_preferences':'Non-Vegetarian', 'budget': '100000'}))
if st.button("Submit"):
    st.write_stream(chain.stream({'username': username, 'destination': destination, 'start_date':start_date, 'end_date':end_date,'interests':interest,'travel_style':travel_style,'dietary_preferences':dietary_preferences, 'budget': budget}))