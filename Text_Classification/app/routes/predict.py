from fastapi import APIRouter
from app.models.schema import TextInput
from app.services.model_service import predict_text

router = APIRouter()

@router.post("/predict")
def predict(data: TextInput):
    result = predict_text(data.text)
    return result