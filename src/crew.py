from crewai import Crew,Agent,Task,Process
from crewai.project import CrewBase,agent,task,crew
from llm import llm
import yaml

def load_yaml(path):
    try:  
        with open(path, 'r') as file:  
            return yaml.safe_load(file)  
    except FileNotFoundError:  
        print(f"File {path} not found.")  
        return {}  
    except Exception as e:  
        print(f"Error loading YAML: {e}")  
        return {} 

@CrewBase
class TripPlannerCrew:
    "The whole crew planing the trip"
    agent_config = load_yaml('src/config/agents.yaml')
    task_config = load_yaml('src/config/tasks.yaml')
    
    @agent
    def trip_details_agent(self) -> Agent:
        return Agent(
            config= self.agent_config['trip_details_agent'],
            tools=[],
            llm=llm
        )
        
    @task
    def trip_data_extractor(self) -> Task:
        return Task(
            config=self.task_config['trip_data_extractor'],
            agent=self.trip_details_agent()
        )
    
    @crew
    def crew(self) -> Crew:
        "Create the Trip planner Crew"
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

    
input = "I want to go to the kandy, Colombo, badulla, Ella. I will stay in sri lanka from 15th of june to 23th of june. my total budhet will be 5000$. I Preferred to use a van for the transportation."

TripPlannerCrew().crew().kickoff(inputs={"input_details": input})
