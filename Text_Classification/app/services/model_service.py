from app.utils.loader import load_model
from app.utils.preprocessing import clean_text

model, vectorizer = load_model()

def predict_text(text: str):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    
    pred = model.predict(vec)[0]
    
    # لو الموديل بيدعم probability
    try:
        proba = model.predict_proba(vec).max()
    except:
        proba = None

    return {
        "input_text": text,
        "prediction": pred,
        "confidence": float(proba) if proba else None
    }