import requests
import os
from dotenv import load_dotenv

from schemas.movie import Movie

load_dotenv()

API_KEY: str = os.getenv("API_KEY")
BASE_URL: str = "http://www.omdbapi.com/"


def get_movie(title: str) -> Movie | None:
    if not API_KEY:
        print("API_KEY não encontrada. Verifique seu .env.")
        return

    params: dict[str, str] = {
        "t": title,
        "apikey": API_KEY
    }

    try:
        response: requests.Response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data: dict[str, str | float] = response.json()

        movie: Movie = Movie(
            data.get("Title"),
            data.get("Year"),
            data.get("Genre"),
            data.get("Type"),
            data.get("Director"),
            data.get("imdbRating")
            )

        return movie
    except requests.HTTPError as e:
        print(f"Erro: {e}")
    return
