from transformers import pipeline

# Multi-class sentiment analysis model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    sentiment = result['label']
    confidence = round(result['score'] * 100, 2)  # converting to percentage for clarity

    # Applying your desired threshold logic:
    if sentiment == 'positive' and confidence < 80:
        sentiment = 'negative'
    elif sentiment == 'negative' and confidence < 80:
        sentiment = 'positive'

    return {
        "sentiment": sentiment,
        "confidence": confidence
    }
