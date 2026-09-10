
# Import FastAPI to create the web application
from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI()


# Define a GET endpoint for the root URL "/"
@app.get("/")
def show():
    # Return a simple Hello World message
    return "Hello World"


# Define a GET endpoint for "/products"
@app.get("/products")
def get_products():
    # Return product information as a dictionary
    return {"name": "laptop", "price": "28638"}


# Define a GET endpoint for "/login"
@app.get("/login")
def login():
    # Return a message indicating that the user is logged in
    return {"message": "loggedin"}


# Check whether this file is being run directly
if __name__ == "__main__":
    # Import Uvicorn, the server used to run the FastAPI application
    import uvicorn

    # Start the FastAPI application using Uvicorn and if issues then reload the server automatically
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
