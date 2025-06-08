from fastapi import FastAPI, UploadFile, File, HTTPException
from app.model import load_model, predict
from app.schemas import PredictResponse

app = FastAPI()

model = load_model()

@app.post("/predict", response_model=PredictResponse)
async def predict_endpoint(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File harus berupa gambar.")
    
    image_bytes = await file.read()
    info = predict(model, image_bytes)
    return PredictResponse(**info)