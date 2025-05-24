import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_sentiment(headlines):
    # Handle different input formats
    if isinstance(headlines, str):
        headlines = [headlines]
    elif not isinstance(headlines, list):
        raise ValueError("Expected a list of strings or a single string for headlines.")

    if not headlines:
        raise ValueError("The headlines list is empty.")

    # Vectorize and predict
    features = vectorizer.transform(headlines)
    return model.predict(features)

