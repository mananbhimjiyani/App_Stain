from fastapi import APIRouter, File, Request, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter()



@router.post("/detect_stain")
async def detect_stain(request: Request, file: UploadFile = File(...)):
    try:
        # Read the uploaded image file
        contents = await file.read()

        # Access the model service from the app state
        model_service = request.app.state.model_service

        # Preprocess the image and get the prediction
        img_array = model_service.preprocess_image(contents)
        predicted_class = model_service.predict(img_array)

        # Return the prediction
        return JSONResponse(content={"prediction": predicted_class})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)