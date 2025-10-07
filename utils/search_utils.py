import os
from serpapi import GoogleSearch
import json

def search_web(query):
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        return "❌ SerpAPI key not found. Please set the SERPAPI_KEY environment variable."

    try:
        search = GoogleSearch({
            "q": query,
            "api_key": api_key,
            "num": 5,
            "engine": "google"
        })
        results = search.get_dict()
        organic_results = results.get("organic_results", [])
        if not organic_results:
            return "No results found."

        response = "🔍 Top results:\n\n"
        for i, result in enumerate(organic_results[:5], start=1):
            title = result.get("title", "No title")
            link = result.get("link", "")
            response += f"{i}. [{title}]({link})\n"
        return response

    except Exception as e:
        return f"⚠️ Search failed: {str(e)}"
