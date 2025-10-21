# utils/search_utils.py
from serpapi import GoogleSearch
import os

def search_web(query):
    try:
        search = GoogleSearch({"q": query, "api_key": os.getenv("SERPAPI_KEY")})
        results = search.get_dict()
        data = results.get("organic_results", [])
        txt = "\n\n".join(f"🔹 *{d.get('title','')}*\n{d.get('link','')}" for d in data[:3])
        return txt
    except Exception as e:
        return f"Error: {e}"
