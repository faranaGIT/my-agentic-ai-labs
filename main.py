from dotenv import load_dotenv
import os

load_dotenv()
print("Loading environment variables from .env file...")
print (os.getenv("MODEL")
       )