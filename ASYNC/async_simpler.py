from groq import AsyncGroq
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables from the .env file.
load_dotenv()

# in this case we have a function that is defined inside another function. This is called a closure. The inner function has access
# to the variables of the outer function, even after the outer function has finished executing. In this case, the inner function a
# sk has access to the client variable defined in the outer function main.
async def main():
    client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

    prompts = [
        "Tell me a joke",
        "What is the capital of India",
        "What is 2+2"
    ]

    async def ask(prompt):
        response = await client.chat.completions.create(
           model=os.getenv("MODEL_NAME", "llama-3.3-70b-versatile"),  # this time we use the model name from the environment variable
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
# * is used to unpack the list of prompts into separate arguments for the ask function. This allows us to send all prompts concurrently and wait for all responses.

    results = await asyncio.gather(*(ask(p) for p in prompts))

    for r in results:
        print(r)


asyncio.run(main())