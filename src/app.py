import logging
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.apis.stain_detection.stain_detection import router as STAIN_DETECTION
from src.model.model_service import ModelService
from .utils.utils import read_markdown_file

# Read README content
readme_content = read_markdown_file("README.md")

# Setup logging
logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger("stain_detection_logger")

app = FastAPI(
    title="Stain Detection",
    description=(lambda: readme_content if isinstance(readme_content, str) else "")(),
    version="1.0.0",
)

@app.on_event("startup")
async def startup_event():
    model_service = ModelService('src/stain_detection.h5')
    app.state.model_service = model_service
    logger.info("Model service initialized.")

app.include_router(STAIN_DETECTION, tags=["Stain detection"])

# Allow all origins (for development purposes)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
