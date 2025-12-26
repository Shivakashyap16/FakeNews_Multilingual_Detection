import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from joblib import dump
from src.preprocess import preprocess

df = pd.read_csv("data/processed/cleaned_data.csv")

processed_texts = []
languages = []

for text in df['text']:
    p_text, lang = preprocess(text)
    processed_texts.append(p_text)
    languages.append(lang)

df['processed_text'] = processed_texts
df['label'] = df['label'].map({'FAKE': 0, 'REAL': 1})

X = df['processed_text']
y = df['label']

vectorizer = TfidfVectorizer(
    analyzer='char_wb',
    ngram_range=(3, 5)
)

X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

print("Model Accuracy:", model.score(X_test, y_test))

dump(vectorizer, "models/tfidf_vectorizer.pkl")
dump(model, "models/naive_bayes_model.pkl")
