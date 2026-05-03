from fastapi import FastAPI
from app.routes.predict import router as predict_router

app = FastAPI(title="Text Classification API")

app.include_router(predict_router)

@app.get("/")
def home():
    return {"message": "API is running 🚀"}