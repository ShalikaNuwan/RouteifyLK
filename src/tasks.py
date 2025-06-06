from crewai import Task
from agents import trip_details_agent

trip_data_extractor = Task(
    description= "extract the trip details from the input prompt {input} given by the user.",
    expected_output= (
        "detailed output of the time period in sri lanka,"
        "the locations where the user wants to go,"
        "prefferes hotels / lodges, meal preferences,"
        "Total budget,"
    ),
    agent=trip_details_agent
)

tasks: list[Task] = [trip_data_extractor]

__all__ = ["tasks"]