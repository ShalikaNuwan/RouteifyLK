from crewai import Crew,Agent,Task,Process
from crewai.project import CrewBase,agent,task,crew
from crewai_tools import SerperDevTool
from .tools import DirectionMapTool
from .llm import llm
import yaml
from pydantic import BaseModel
from typing import List

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

class Attraction(BaseModel):
    name: str
    distance: str
    time_to_visit: str
    cost: str

class Restaurant(BaseModel):
    name: str
    meal_cost: str
    specialty: str

class Location(BaseModel):
    city: str
    attractions: List[Attraction]
    restaurants: List[Restaurant]

class OutputModel(BaseModel):
    locations: List[Location]


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
        
    @agent
    def path_finder_agent(self) -> Agent:
        direction_tool = DirectionMapTool()
        return Agent(
            config= self.agent_config['path_finder_agent'],
            tools=[direction_tool],
            llm=llm
        )
    
    @agent
    def location_details_agent(self) -> Agent:
        return Agent(
            config=self.agent_config['location_details_aegnt'],
            tools=[SerperDevTool()],
            llm=llm
        )
    
    @task
    def trip_data_extractor(self) -> Task:
        return Task(
            config=self.task_config['trip_data_extractor'],
            agent=self.trip_details_agent()
        )
    
    @task
    def find_best_path(self) -> Task:
        return Task(
            config=self.task_config['find_best_path'],
            agent=self.path_finder_agent(),
            context=[self.trip_data_extractor()]
        )
    
    @task
    def find_locations_resturant(self) -> Task:
        return Task(
            config=self.task_config['find_locations_resturants'],
            agent=self.location_details_agent(),
            context=[self.find_best_path(),self.trip_data_extractor()],
            output_json=OutputModel,
            output_file='locations.json'
            
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

def runplanner(input):
    TripPlannerCrew().crew().kickoff(inputs={"input_details": input})
