from crewai import Agent
from llm import llm
from crewai.tools import tool

@tool('getUserInput')
def getInputFromTheUser() -> str:
    "User will give the input for the trip details"
    user_input = "I want to go to the kandy, Colombo, badulla, Ella. I will stay in sri lanka from 15th of june to 23th of june. my total budhet will be 5000$. I Preferred to use a van for the transportation."
    # user_input = input('Enter the trip details') 
    return user_input


#Agent to understand the user preferenes for the trip.
trip_details_agent = Agent(
    role="Understand the user preferences for the trip.",
    goal=(
        "Extract the trip details of {input_details} from the user, including the cities they want to visit, the duration of the trip, total buddget, Hotel type, meal preferences and any specific activities they want to do. "
    ),
    backstory="You are a smart assistant to understand the user preferences for the trip.",
    llm=llm,
    tools=[getInputFromTheUser]
)

agents: list[Agent] = [trip_details_agent]

__all__ = ["agents", "trip_details_agent"]
