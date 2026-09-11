from openrouter import OpenRouter
from dotenv import load_dotenv
import os
import chromadb

load_dotenv()


# Funtion to generate embeddings
# same as main.py and embedding_working.py, you can use this function to generate embeddings for any text
def generate_embeddings(text: str):
    client = OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY"))
    response = client.embeddings.generate(
        model="openai/text-embedding-3-small",
        input=text,
        dimensions=534
    )
    return response.data[0].embedding


# Path of the chromadb database file
# this is the path where the chromadb database file will be stored, you can change it to any other path based on your requirement
CHROMA_PATH = "./chroma_storage"

# Create an instance of Chroma Client
# creates a new database file if it does not exist, otherwise it will connect to the existing database file
client = chromadb.PersistentClient(path=CHROMA_PATH)

# Create a new collection in db
# if the collection already exists, it will return the existing collection
collection = client.get_or_create_collection(
    name="travel_knowledge"
)

# Example Documents
docs = [
    "The Eiffel Tower in Paris is a wrought-iron structure known for its iconic design and panoramic city views.",
    "The Great Wall of China is an ancient series of fortifications built to protect against invasions and spans thousands of miles.",
    "The Statue of Liberty in New York symbolizes freedom and democracy, and was a gift from France to the United States."
]

# 1- first Generate embeddings for each document
doc_emeddings = [generate_embeddings(doc) for doc in docs]


# 2- after that Add document embeddings in vector database
# we are storing the actual document, its embedding, a unique id for each document and some metadata in the vector database
def create_documents():
    collection.add(
        documents=docs,
        embeddings=doc_emeddings,
        ids=["doc1", "doc2", "doc3"],
# metadata is optional, you can store any additional information about the document in metadata,
#  it can be useful for filtering or searching documents based on metadata
# instead of sample1 we can store the actual document name or any other information about the document in metadata
        metadatas=[
            {"source": "sample1"},
            {"source": "sample2"},
            {"source": "sample3"},
        ]
    )
    print("Documents successfully added to ChromaDB")


# 3- Retrieve all documents
# we can get the documents or ids or embeddings or metadata from the vector database, 
# here we are retrieving all the documents from the vector database
def get_documents():
    result = collection.get(include=['embeddings'])
    print(result['embeddings'])


# 4- Update the documents based on document id
# we want embeddings for the document "The Taj Mahal is located in Agra, India, and is a UNESCO World Heritage Site." 
# and we want to update the document with id "doc1" in the vector database
def update_documents(id: str):
    collection.update(
        ids=[id],
        embeddings=[generate_embeddings(
            "The Taj Mahal is located in Agra, India, and is a UNESCO World Heritage Site."
        )],
        documents=[
            "The Taj Mahal is located in Agra, India, and is a UNESCO World Heritage Site."
        ]
    )
    print("Document Updated")


# 5- Delete document based on Id
def delete_documents(id: str):
    collection.delete(ids=[id])
    print("Document Delete")

# from 2 to 5 we can call the functions based on our requirement,
#  for example if we want to add documents in the vector database,
#  we can call the function
# currently none of the functions are called, you can call the functions based on your requirement

#1 - create the documents in the vector database
# not how the chromar_storage db is created in the current directory, you can change the path in CHROMA_PATH variable based on your requirement
create_documents()

