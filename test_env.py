from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

if key:
    print(" API Key found:", key[:10], "...")  # Only shows first 10 characters for safety
else:
    print(" API Key NOT found. Check your .env file")