from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load the pre-trained BERT model (use a fine-tuned model if available)
model = pipeline('text-classification', model='bert-base-uncased')


class NewsArticle(BaseModel):
    text: str


@app.post("/predict")
async def predict(news_article: NewsArticle):
    if not news_article.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty")

    try:
        prediction = model(news_article.text)
        return {"label": prediction[0]['label'], "confidence": prediction[0]['score']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during prediction: {str(e)}")

model = pipeline('text-classification', model='./fine_tuned_model', tokenizer='./fine_tuned_model')
