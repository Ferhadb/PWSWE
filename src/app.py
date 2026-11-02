# src/app.py
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


# Define a route for the home page ("/")
@app.get("/", response_class=PlainTextResponse)
def index():
    """Returns a simple Hello, World! string."""
    return "Hello, World!"


# Define a dynamic route that accepts a name in the URL
@app.get("/greet/{name}", response_class=PlainTextResponse)
def greet(name: str):
    """Returns a personalized greeting."""
    return f"Hello, {name}!"
