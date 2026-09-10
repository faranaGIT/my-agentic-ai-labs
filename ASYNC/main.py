
from groq import AsyncGroq
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables from the .env file.
load_dotenv()

# Create an asynchronous Groq client using the API key to make an aync call to llm
# stored in the GROQ_API_KEY environment variable.
client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))


# Define an asynchronous function that sends a prompt
# to the Groq API and returns the AI's response.
async def ask(prompt):

    # Send the prompt to the specified Groq model.
    response = await client.chat.completions.create(
        model=os.getenv("MODEL_NAME", "llama-3.3-70b-versatile"),  # this time we use the model name from the environment variable
        messages=[{"role": "user", "content": prompt}],
    )

    # Extract and return the text of the AI's response.
    return response.choices[0].message.content


# Define the main asynchronous function. means the tasks happen all at once, not one after the other. This is called concurrency.
async def main():

    # Create a list of prompts that we want to send to the AI.
    prompts = ["Tell me a joke", "What is the capital of India", "What is 2+2"]

    # Send all prompts concurrently and wait for all responses.
    # * is used to unpack the list of prompts into separate arguments for the ask function. This allows us to send all prompts concurrently and wait for all responses.
    results = await asyncio.gather(*(ask(p) for p in prompts))

    # Loop through each response and print it.
    for r in results:
        print(r)

# Start the main asynchronous function.
asyncio.run(main())
