import os
from serpapi.google_search import GoogleSearch
def search_web(query: str):
    try:
        search = GoogleSearch({
            "q": query,
            "api_key": os.getenv("SERPAPI_KEY")
        })
        results = search.get_dict()
        return results.get("organic_results", [])
    except Exception as e:
        return [{"title": f"Error: {e}", "link": ""}]
