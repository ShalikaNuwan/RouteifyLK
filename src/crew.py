from crewai import Crew
from agents import agents
from tasks import tasks

crew = Crew(
    agents=agents,
    tasks=tasks,
    verbose=True
)

crew.kickoff()