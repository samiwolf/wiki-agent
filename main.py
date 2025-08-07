import google.generativeai as genai
import wikipedia
from dotenv import load_dotenv
import os
import re

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash-latest')

topic = "Football"

related_response = model.generate_content(f"Give me 5 related topics to: {topic}")
related_topics = related_response.text.split('\n')

for t in related_topics:
    try:
        info = wikipedia.summary(t, sentences=3)
        explanation_response = model.generate_content(f"Explain this simply: {info}")
        for chunk in explanation_response:
            print(chunk.text)
    except Exception as e:
        print(f"Failed for {t}: {e}")
