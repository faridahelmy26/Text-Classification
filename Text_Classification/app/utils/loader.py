import joblib

def load_model():
    model = joblib.load("model/logistic_regression_model.pkl")
    vectorizer = joblib.load("model/tfidf_vectorizer.pkl")
    return model, vectorizer