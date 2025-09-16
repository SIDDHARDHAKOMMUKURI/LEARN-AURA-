# utils/serp_api.py
import os
import requests

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def serp_search(query: str, num: int = 5):
    if not SERPAPI_KEY:
        return []
    # Example using SerpAPI (user must adapt to real SerpAPI endpoint)
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": num
    }
    # Replace with actual SerpAPI endpoint & param scheme
    resp = requests.get("https://serpapi.com/search", params=params, timeout=10)
    data = resp.json()
    results = []
    for item in data.get("organic_results", [])[:num]:
        results.append({"title": item.get("title"), "link": item.get("link")})
    return results
