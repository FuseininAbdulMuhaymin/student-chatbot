# from google import genai
# from dotenv import load_dotenv
# import os


# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY ")

# #confirguring gemini model
# Client = genai.Client(api_key)
# model = genai.GenerativeModel("gemini-1.5-flash")

# SYSTEM_PROMPT = """
#   You are a helpful assistant for students who assisant

#   Your job is to :
#   -Help Students learn
#   -Explain difficult concepts in simply
#   -Answer questions about a wide range of clearly
#   - Be friendly and professional
#   - Give step-by-step explanations
# """
# chat_history = []

# def user_chat():

#     return {
#         "history":[]
#     }

# def   send_message(chat_session, user_message):
#     chat_session["history"].append({
#         "role":"user",
#         "content":user_message
#       })

from google import genai
from dotenv import load_dotenv
import os


# LOAD ENVIRONMENT VARIABLES

load_dotenv()
# GET API KEY

api_key = os.getenv("GEMINI_API_KEY")
# CREATE CLIENT
client = genai.Client(api_key=api_key)
# SYSTEM PROMPT
SYSTEM_PROMPT = """
You are a helpful AI study assistant.

Your job is to:
- Help students learn
- Explain concepts simply
- Answer questions clearly
- Be friendly and professional
- Give step-by-step explanations

Always respond in a beginner-friendly way.
"""
# START CHAT
def start_chat():

    return {
        "history": []
    }

# SEND MESSAGE
def send_message(chat_session, user_message):

    # Save user message
    chat_session["history"].append({
        "role": "user",
        "content": user_message
    })

    # Build full prompt
    full_prompt = SYSTEM_PROMPT + "\n\n"

    for message in chat_session["history"]:

        role = message["role"]
        content = message["content"]

        full_prompt += f"{role}: {content}\n"

    # GENERATE RESPONSE

    response = client.models.generate_content(
       model="gemini-1.5-flash-001",
        contents=full_prompt
    )

    # Get AI text
    ai_response = response.text

    # Save AI response
    chat_session["history"].append({
        "role": "assistant",
        "content": ai_response
    })

    return ai_response