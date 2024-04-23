from pydantic import BaseModel
from fastapi import FastAPI
from model import *

import warnings
warnings.simplefilter("ignore")


# Init the application
app = FastAPI()

# Load the api here
api = LLMApi()

# Pydantic model for the data
class InputFormat(BaseModel):
    question: str
    user_response: str
    correct_response: str
    
class ResponseFormat(BaseModel):
    output: str
    search_results: list

@app.post("/get_help/", response_model=ResponseFormat)
async def create_item(input_format: InputFormat):
    output, queries = api.get_suggestions(input_format.question, input_format.user_response, input_format.correct_response)
    search_results = api.get_google_results(queries)
    return {"output": output, "search_results": search_results}