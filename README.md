# Sentiment-Analysis

This project is a lightweight web application that performs sentiment analysis on social media content or user-submitted text. Using Python's Flask framework and TextBlob library, it classifies the input as Positive, Negative, or Neutral in real-time.

---

## 💡 Overview

Sentiment analysis is a core task in natural language processing (NLP), used to determine the emotional tone of text data. This web app demonstrates a simple pipeline using:

* Flask for backend web server
* TextBlob for natural language processing and sentiment scoring
* HTML/CSS for the frontend

It's a great starting point for understanding text classification and building practical AI applications.

---

## 🛠️ Features

* 🔎 Real-time text sentiment analysis
* 🌐 Web interface for user interaction
* 🎯 Three-label classification: Positive, Neutral, Negative
* 🧠 Polarity scoring using TextBlob

---

## 🧰 Tech Stack

* Python 3.x
* Flask (for backend)
* TextBlob (for sentiment scoring)
* HTML + CSS (for frontend UI)

---

## 📦 Installation & Setup

### 1. Clone or Download the Project

```bash
git clone https://github.com/your-repo/sentiment-analysis-app.git
cd sentiment-analysis-app
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install flask textblob
python -m textblob.download_corpora
```

### 4. Run the App

```bash
python sentiment_app.py
```

Then open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Example Inputs

| Input                                | Output   |
| ------------------------------------ | -------- |
| "I love this product!"               | Positive |
| "It's okay, nothing great."          | Neutral  |
| "I absolutely hate waiting in line." | Negative |

---

## 🧠 How It Works

1. User inputs a sentence or social media text into the form.
2. The Flask backend receives the input and passes it to TextBlob.
3. TextBlob calculates the polarity score (-1 to 1):

   * > 0.1 → Positive
   * < -0.1 → Negative
   * Between -0.1 and 0.1 → Neutral
4. The sentiment result is sent back and displayed on the frontend.

---

## 🧱 Project Structure

```
sentiment_analysis_app/
├── sentiment_app.py               # Flask backend logic
├── templates/
│   └── sentiment_frontend.html    # HTML form and UI
└── README.md                      # Project overview
```

---

## 🚀 Future Enhancements

* 🤖 Use more advanced NLP models (VADER, BERT, LSTM)
* 📊 Add visual analytics and sentiment trend tracking
* 🗃️ Support for file upload and batch sentiment analysis
* 🌍 Deploy to Heroku or Render for public access

---

## 🙋‍♂️ Author

Built by Sanjay Narasimhan — a software developer and AI enthusiast.
