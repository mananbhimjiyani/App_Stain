import uvicorn
from src.app import app  # Assuming your FastAPI app is in src/app.py

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
