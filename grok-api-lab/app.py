import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1",
)

print("Sending request to Grok...")

response = client.chat.completions.create(
    model="grok-4.7",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain artificial intelligence in simple terms."},
    ],
)

print("\nGrok response:")
print(response.choices[0].message.content)