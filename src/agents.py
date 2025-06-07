from crewai import Agent
from llm import llm
from crewai.tools import tool

# trip_details_agent = Agent(
#     role="Understand the user preferences for the trip.",
#     goal=(
#         "Extract the trip details of {input_details} from the user, including the cities they want to visit, the duration of the trip, total buddget, Hotel type, meal preferences and any specific activities they want to do. "
#     ),
#     backstory="You are a smart assistant to understand the user preferences for the trip.",
#     llm=llm,
#     tools=[]
# )

# agents: list[Agent] = [trip_details_agent]

# __all__ = ["agents", "trip_details_agent"]
