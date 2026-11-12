
from pathlib import Path
from io import BytesIO
import pandas as pd

from fastapi import UploadFile, File, HTTPException
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.services.metadata import discover_metadata

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


@app.post("/api/datasets/preview")
async def preview_dataset(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are supported"
        )
    
    contents = await file.read()
    max_size = 10 * 1024 * 1024

    if len(contents) > max_size:
        raise HTTPException(
            status_code=413,
            detail="File exceeds the 10 MB limit"
        )

    if not contents:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty"
        )

    try:
        df = pd.read_csv(BytesIO(contents))
    except (pd.errors.ParserError, UnicodeDecodeError, ValueError):
        raise HTTPException(
            status_code=400,
            detail="Unable to read this CSV file"
        )

    # dt profilling
    if df.empty:
        raise HTTPException(
            status_code=400,
            detail="The CSV contains no data rows"
        )

    if len(df.columns) == 0:
        raise HTTPException(
            status_code=400,
            detail="The CSV contains no columns"
        )

    columns = discover_metadata(df)

    sample = (
        df.head(5)
        .astype(object)
        .where(pd.notna(df.head(5)), None)
        .to_dict(orient="records")
    )

    return {
        "filename": file.filename,
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "columns": columns,
        "sample_data": sample
    }


frontend_directory = Path(__file__).resolve().parents[2] / "frontend"

app.mount(
    "/",
    StaticFiles(directory=frontend_directory, html=True),
    name = "frontend"
)
