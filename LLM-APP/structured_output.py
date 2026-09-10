from pydantic import BaseModel, Field
from typing import Literal
# this is from the common.py file where we have defined the get_client function to get the anthropic client

from common import get_client

class Feedback(BaseModel):
    name: str = Field(description="Name of the participant")
    summary: str = Field(description="Summary of the overall feedback")
    sentiment: Literal['positive', 'negative'] = Field(description="Sentiment of the feedback like positive or negative")
    rating: int = Field(description="Rating of the feedback provided by participant")
    email: str =Field(description="Email adresss of the participant")

client = get_client()
response = client.messages.create(
    model="claude-sonnet-4-5",
    system="You are a helpful AI assistant who structures the input in a specific model and identifies the sentiment of the feedback",
    messages=[{
        "role": "user",
        "content": "The Java Fullstack training program was well-structured and covered essential modules like Core Java, Spring Boot, Hibernate, and Angular. The hands-on projects and live coding sessions made it easier to apply concepts in real-world scenarios. The trainer was knowledgeable and supportive, and the sessions on Git and deployment provided a complete view of end-to-end development. However, the pace during the Spring Boot section felt a bit fast, and more time for practice would have been helpful. Additionally, a dedicated session on debugging and code optimization could enhance the learning experience. Some front-end sessions, especially on Angular, felt rushed, and could benefit from more real-time examples. Out of 5 I would give 4 rating for this program. Feedback given by Dhiraj Kumar. Email address - dhiraj2001@gmail.com"
    }],
    max_tokens=500,
    tools=[{
        "name": "output_format",
        "description": "Return the structured output",
        "input_schema": Feedback.model_json_schema()
    }],
    tool_choice={"type": "tool", "name": "output_format"}
)
print(response)