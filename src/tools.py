from crewai.tools import BaseTool
from pydantic import BaseModel
import requests
from dotenv import load_dotenv
import os


class DirectionMap(BaseModel):
    origin : str
    destination : str
    mode: str = 'driving'
    
class DirectionMapTool(BaseTool):
    name:str = "GoogleMapDirections"
    description:str = "get the distance and duration between two locations using the Google map"
    args_schema:type[BaseModel] = DirectionMap
    
    def _run(self, origin:str, destination:str,mode: str='driving'):
        load_dotenv()
        api_key = os.getenv('GOOGLE_MAPS_API_KEY')
        url = "https://maps.googleapis.com/maps/api/directions/json"
        params = {
            "origin": origin,
            "destination": destination,
            "mode": mode,
            "key": api_key
        }
        response = requests.get(url, params=params).json()

        if response["status"] != "OK":
            return f"Error: {response['status']}"

        leg = response["routes"][0]["legs"][0]
        distance = leg["distance"]["text"]
        duration = leg["duration"]["text"]
        steps = [step["html_instructions"] for step in leg["steps"]]
        
        return f"From {origin} to {destination} ({mode}):\nDistance: {distance}\nDuration: {duration}\nSteps:\n" + "\n".join(steps)
