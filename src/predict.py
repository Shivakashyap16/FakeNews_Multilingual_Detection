from joblib import load
from src.preprocess import preprocess

vectorizer = load("models/tfidf_vectorizer.pkl")
model = load("models/naive_bayes_model.pkl")

LANGUAGE_MAP = {
    "en": "English",
    "hi": "Hindi",
    "te": "Telugu"
}

def predict_news(text):
    processed_text, lang_code = preprocess(text)
    vector = vectorizer.transform([processed_text])
    prediction = model.predict(vector)[0]

    language = LANGUAGE_MAP.get(lang_code, "Unknown")

    if prediction == 1:
        return "REAL NEWS", language
    else:
        return "FAKE NEWS", language
