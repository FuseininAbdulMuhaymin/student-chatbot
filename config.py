import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create client (THIS replaces configure)
client = genai.Client(api_key=api_key)

# Send a simple request (THIS replaces model creation)
response = client.models.generate_content(
    model="gemini-1.5-flash-001",
    contents="Hello"
)

print(response.text)