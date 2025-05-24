import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def get_sentiment_summary(news_headlines):
    prompt = f"""
Analyze the following stock market news headlines for sentiment (positive, neutral, negative):

{news_headlines}

Summarize the overall sentiment in 2-3 lines.
"""
    response = model.generate_content(prompt)
    return response.text

