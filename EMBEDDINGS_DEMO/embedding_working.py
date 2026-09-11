from openrouter import OpenRouter
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os

load_dotenv()

# Funtion to generate embeddings
def generate_embeddings(text: str):
    client = OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY"))
    response = client.embeddings.generate(
        # this is the model used to generate embeddings, you can use any other embedding model available in OpenRouter
        model="openai/text-embedding-3-small",
        input=text,
        dimensions=534
    )
    # this is the embedding vector for the input text, you can use this vector to perform similarity search or other tasks
    return response.data[0].embedding

print("Generating embeddings for documents and query...")
# this will show if the embeddings are generated successfully or not
# if the model is working fine, it will return a list of embeddings for each document and the query

print(generate_embeddings("The Eiffel Tower is in Paris"))