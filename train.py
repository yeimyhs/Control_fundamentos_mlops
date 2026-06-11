from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

texts = [
    "Win money now",
    "Claim your prize",
    "Free gift card",
    "Meeting tomorrow at 10",
    "Please send the report",
    "Let's have lunch"
]

labels = [
    "spam",
    "spam",
    "spam",
    "ham",
    "ham",
    "ham"
]

model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

model.fit(texts, labels)

joblib.dump(model, "model.pkl")

print("Modelo guardado.")