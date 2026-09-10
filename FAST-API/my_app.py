
# don't forget to install the required packages before running this code:
# uv add pydantic groq python-dotenv 
# don't forget to copy the .env.example file to .env and set your GROQ_API_KEY in the .env file
#    
# Import FastAPI to create the web application
from fastapi import FastAPI

# Import BaseModel to define and validate request/response data
from pydantic import BaseModel

# Import Groq to connect to the Groq API
from groq import Groq

# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Import os to access environment variables
import os


# Load environment variables from the .env file
load_dotenv()

# Create an instance of the FastAPI application
app = FastAPI()

# Create a Groq client using the API key stored in the environment variables
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#aim of this app is to provide a simple API endpoint that takes a user's prompt and returns a
#  generated response from the Groq AI model. 
# The app uses FastAPI for handling HTTP requests and Pydantic for data validation.


# Define the structure of the incoming request
class PromptRequest(BaseModel):
    # The message field contains the user's prompt
    message: str


# Define the structure of the response sent back to the user
class PromptResponse(BaseModel):
    # Contains the generated response from the AI model
    message: str

    # Contains the name of the AI model being used
    model: str

    # Contains the status of the request
    status: str


# Define a POST endpoint at "/generate"
@app.post("/generate")
def generate(request: PromptRequest):

    # Send the user's message to the Groq AI model
    response = client.chat.completions.create(
        # Specify the AI model to use
        model="llama-3.3-70b-versatile",

        # Provide the user's message to the model
        messages=[{"role": "user", "content": request.message}],

        # Control the randomness/creativity of the generated response
        temperature=0.8
    )

    # Return the generated response using the PromptResponse model
    return PromptResponse(
        # Get the generated text from the first response choice
        message=response.choices[0].message.content,

        # Return the name of the AI model used
        model="llama-3.3-70b-versatile",

        # Indicate that the request was successful
        status="success"
    )


# Check whether this file is being run directly
if __name__ == "__main__":

    # Import Uvicorn, the server used to run the FastAPI application
    import uvicorn

    # Start the FastAPI application using Uvicorn
    uvicorn.run("my_app:app", host="localhost", port=8000, reload=True)