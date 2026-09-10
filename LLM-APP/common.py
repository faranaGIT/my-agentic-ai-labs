import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

#here we are using the OpenRouter API base URL for the Anthropics client
OPENROUTER_BASE_URL="https://openrouter.ai/api"

# the op
def get_client():
    return anthropic.Anthropic(auth_token=os.getenv("OPENROUTER_API_KEY"), base_url=OPENROUTER_BASE_URL)