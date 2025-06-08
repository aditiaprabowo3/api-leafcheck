from pydantic import BaseModel

class PredictResponse(BaseModel):
    penyakit: str
    penjelasan: str
    solusi: str