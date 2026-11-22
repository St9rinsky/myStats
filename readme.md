
# myStats


myStats allows users to upload datasets and ask natural-language questions to obtain analytical insights backed by their actual data

## flow

- upload csv
- data profilling : Discover columns, data types, missing values, duplicates, unique values, and distributions.
- Data processing : Clean data where appropriate, calculate statistics, group records, compare populations, and identify patterns.
- ai analysis : Interpret the question, determine which analyses are needed, and explain the resulting evidence.
- Business insight

## Current Features

- FastAPI backend
- Web-based interface
- Backend health-check endpoint

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- Pandas
- HTML
- CSS
- Js

## Running Locally

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd myStats
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate it

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 5. Start the backend

```bash
cd backend
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000

## Project Status

Early development.
