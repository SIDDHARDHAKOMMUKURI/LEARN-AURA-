# utils/gemini_api.py
import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY")

def ask_gemini(prompt: str) -> str:
    """
    Placeholder wrapper. Replace with actual Gemini/OpenAI request.
    Example: Use OpenAI Chat Completions or Gemini REST API.
    """
    if not GEMINI_API_KEY:
        return "(AI not configured) " + prompt

    # Example: Simple OpenAI-compatible call (user should replace with correct API usage)
    try:
        # If you use OpenAI:
        # import openai; openai.api_key = GEMINI_API_KEY
        # resp = openai.ChatCompletion.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt}])
        # return resp.choices[0].message.content
        return f"[AI placeholder answer for] {prompt}"
    except Exception as e:
        return f"(AI error) {e}"
