from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    while True:
        user_input = input("You: ") # this is why we get the user input from the console
        if user_input.lower()=="exit":
            break

        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
           messages=[{"role": "user", "content": user_input}, {"role": "system", "content": ""}],
          # messages=[{"role": "user", "content": "When is christmas 2045"}],
            temperature=0.3,
           max_tokens=2000 #sets max tokens for the response
        )
        print(f"AI: {response.choices[0].message.content}")

if __name__ == "__main__":
    main()
