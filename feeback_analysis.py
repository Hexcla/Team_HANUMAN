from textblob import TextBlob

def analyze_feedback(feedback):
    blob = TextBlob(feedback)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score

feedbacks = [
    "The ride was great, very comfortable!",
    "Driver was late, not happy with the service.",
    "Overall, a decent experience."
]

sentiments = [analyze_feedback(feedback) for feedback in feedbacks]
print("Sentiment scores:", sentiments)
