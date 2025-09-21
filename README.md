# uniplane-costsight

A FastAPI microservice for Uniplane.

## Run locally
```bash
uvicorn app.main:app --reload
```

## Build & Run with Docker
```bash
docker build -t uniplane-costsight .
docker run -p 8000:8000 uniplane-costsight
```
