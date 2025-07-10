from fastapi import FastAPI
from typing import Optional
import json
from fastapi.middleware.cors import CORSMiddleware
from src.crew import runplanner

app = FastAPI()

origins = [
    "http://localhost:8081",  # React dev server
    "http://172.20.10.3:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for all origins (not safe for prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/mainRoute')
def root(siteName: Optional[str] = ''):
    runplanner(siteName)
    
    with open('locations.json', 'r') as file:
        data = json.load(file)
        
    return data


    
    