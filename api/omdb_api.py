import requests
import os
from dotenv import load_dotenv

from schemas.movie import MovieBase, MovieDetail

load_dotenv()

API_KEY: str = os.getenv("API_KEY")
BASE_URL: str = "http://www.omdbapi.com/"


def get_movie(title: str) -> MovieDetail | None:
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

        if data.get("Response") == "False":
            print(data.get("Error", "Erro ao buscar filme."))
            return None

        return MovieDetail(
            data.get("Title"),
            data.get("Year"),
            data.get("Genre"),
            data.get("Type"),
            data.get("Director"),
            data.get("imdbRating")
            )
    except requests.HTTPError as e:
        print(f"Erro: {e}")
    return


def search_movies_by_keyword(keyword: str) -> list[MovieBase] | None:
    if not API_KEY:
        print("API_KEY não encontrada. Verifique seu .env.")
        return

    params: dict[str, str] = {
        "s": keyword,
        "apikey": API_KEY
    }

    try:
        response: requests.Response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data: dict[str, str | float] = response.json()

        if data.get("Response") == "False":
            print(data.get("Error", "Erro ao buscar filme."))
            return None

        search_results: list[dict[str, str]] = data.get("Search", [])

        return [
            MovieBase(
                movie.get("Title"),
                movie.get("Year"),
                movie.get("Type"),
            )
            for movie in search_results
        ]
    except requests.HTTPError as e:
        print(f"Erro na requisição: {e}")
        return
