# Sentiment Analysis on Social Media using TextBlob and Flask
# Requirements: flask, textblob, nltk, sklearn (optional for model training)

from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sentiment_frontend.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form['user_input']
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return render_template('sentiment_frontend.html', input_text=user_input, result=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
