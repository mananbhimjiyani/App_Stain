import os
import uvicorn
from src.app import app  # Adjust to your app's path

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Fetch the port from the environment
    uvicorn.run(app, host="0.0.0.0", port=port)  # Bind to 0.0.0.0 and use the dynamic port
