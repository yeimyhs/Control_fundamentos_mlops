from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

class Message(BaseModel):
    text: str

@app.post("/predict")
def predict(msg: Message):
    prediction = model.predict([msg.text])[0]
    return {"prediction": prediction}