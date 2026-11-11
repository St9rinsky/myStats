
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="myStats",
    description="An AI analysis platform",
    version="0.1.0"
)


@app.get("/api/health")
def health_check():
    return {
        "application": "myStats",
        "status": "running",
        "version": "0.1.0"
    }


frontend_directory = Path(__file__).resolve().parents[2] / "frontend"

app.mount(
    "/",
    StaticFiles(directory=frontend_directory, html=True),
    name = "frontend"
)
