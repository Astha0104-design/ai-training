import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# The client automatically picks up the GEMINI_API_KEY environment variable
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash-lite", 
    contents="Explain artificial intelligence in simple terms."
)

print(response.text)