import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
if not API_KEY:
    raise RuntimeError("TMDB_API_KEY not found in .env")

API_URL = f"https://api.themoviedb.org/3/tv/popular?api_key={API_KEY}"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

def fetch_and_save():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        shows = []
        for item in data["results"]:
            if item.get("poster_path"):
                shows.append({
                    "title": item["name"],
                    "image": IMAGE_BASE_URL + item["poster_path"]
                })

        output_path = "../shared/shows.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(shows, f, indent=2)

        print(f"Saved {len(shows)} shows to {output_path}")

    except Exception as e:
        print("Error fetching or saving data:", e)

if __name__ == "__main__":
    fetch_and_save()
