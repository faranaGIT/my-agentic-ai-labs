from openrouter import OpenRouter
import os
from dotenv import load_dotenv

load_dotenv()

with OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY")) as client:
    response = client.chat.send(
       # model="openai/gpt-4o-mini",
        model="~anthropic/claude-haiku-latest",
        messages=[
            {"role": "user", "content": "Give me a single sentence motivational quote."}  
        ] 
    )

    print(response.choices[0].message.content)