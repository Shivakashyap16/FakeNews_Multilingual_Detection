import re
import nltk
from langdetect import detect
from indicnlp.tokenize import indic_tokenize

nltk.download('stopwords')
from nltk.corpus import stopwords

english_stopwords = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\u0900-\u097F\u0C00-\u0C7F\s]", "", text)
    return text

def tokenize_text(text, lang):
    if lang == 'en':
        words = text.split()
        words = [w for w in words if w not in english_stopwords]
        return " ".join(words)
    else:
        tokens = indic_tokenize.trivial_tokenize(text)
        return " ".join(tokens)

def preprocess(text):
    cleaned = clean_text(text)
    try:
        lang = detect(cleaned)
    except:
        lang = 'en'
    processed = tokenize_text(cleaned, lang)
    return processed, lang
