# utils/sentiment_utils.py
from textblob import TextBlob

def analyze_sentiment(text: str) -> dict:
    """
    Simple sentiment using TextBlob polarity:
      polarity in [-1.0, 1.0], >0 positive, <0 negative, ~0 neutral
    """
    blob = TextBlob(text)
    pol = blob.sentiment.polarity
    if pol > 0.1:
        label = "Positive"
    elif pol < -0.1:
        label = "Negative"
    else:
        label = "Neutral"
    return {"label": label, "score": pol}
