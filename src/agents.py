from crewai import Agent
from llm import llm


#Agent to understand the user preferenes for the trip.
trip_details_agent = Agent(
    role="Understand the user preferences for the trip.",
    goal=(
        "Extract the trip details from the user, including the cities they want to visit, the duration of the trip, total buddget, Hotel type, meal preferences and any specific activities they want to do. "
    ),
    llm=llm
)

agents: list[Agent] = [trip_details_agent]

__all__ = ["agents", "trip_details_agent"]
