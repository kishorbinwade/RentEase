import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from fastapi.responses import FileResponse

# Load .env file
load_dotenv()

app = FastAPI(title=os.getenv("API_NAME", "FastAPI"))

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set full path to static/templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/api")
def api_message():
    return {"message": f"Welcome to {os.getenv('API_NAME', 'API')} from FastAPI backend!"}


@app.get("/")
def serve_react():
    index_path = os.path.join(BASE_DIR, "static", "index.html")
    return FileResponse(index_path)
