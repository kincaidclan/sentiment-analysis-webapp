# Real-Time Sentiment Analysis Web App

This web application provides real-time sentiment analysis powered by advanced Natural Language Processing (NLP). Using FastAPI and Hugging Face Transformers, the application accurately classifies user-input text as either positive or negative sentiment, incorporating an adjustable confidence threshold to handle nuanced and ambiguous statements effectively.

## 🚀 Features

- **Real-Time Analysis:** Instantly analyze the sentiment of user-input text.
- **Advanced NLP Model:** Utilizes a pre-trained Transformer model (`twitter-roberta-base-sentiment-latest`).
- **Adjustable Confidence Threshold:** Ambiguous statements below a confidence level of 80% are automatically flipped to ensure nuanced accuracy.
- **User-Friendly Interface:** Clean and intuitive frontend built with HTML, CSS, and JavaScript.

## 🛠️ Technologies Used

- **Backend:** FastAPI (Python)
- **NLP Engine:** Hugging Face Transformers
- **Frontend:** HTML, CSS, JavaScript

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/kincaidclan/sentiment-analysis-webapp.git
cd sentiment-analysis-webapp
```

Create and activate a Python virtual environment:

```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

## 🚦 Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open your web browser and navigate to:

```
http://127.0.0.1:8000
```

## 🔄 API Endpoint

### Analyze Sentiment

Make a POST request to `/analyze`:

```json
{
  "text": "Your text here"
}
```

Example response:

```json
{
  "sentiment": "positive",
  "confidence": 92.3
}
```

## 📌 Confidence Threshold Logic

- Sentiments labeled as **positive** with confidence below **80%** are flipped to **negative**.

## 🌐 Deployment

You can deploy this application easily on platforms like:

- [Render](https://render.com)
- [Hugging Face Spaces](https://huggingface.co/spaces)
- [Azure App Service](https://azure.microsoft.com)

## 🤝 Contribution

Contributions and suggestions are welcome. Please fork the repository and create a pull request.


