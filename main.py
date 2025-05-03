import requests
import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://www.omdbapi.com/"


@dataclass
class Movie:
    title: str
    year: int
    genre: str
    director: str
    imdbRating: float


def get_movie(title):
    if not API_KEY:
        print("API_KEY não encontrada. Verifique seu .env.")
        return

    params = {
        "t": title,
        "apikey": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()

        movie = Movie(
            data.get("Title"),
            data.get("Year"),
            data.get("Genre"),
            data.get("Director"),
            data.get("imdbRating")
            )

        return movie
    except requests.HTTPError as e:
        print(f"Erro: {e}")
    return


if __name__ == "__main__":
    while True:
        title = input("\nDigite o nome de um filme (ou 'sair'): ").strip()
        if title.lower() == 'sair':
            break
        movie = get_movie(title.replace(" ", "+"))

        print(movie)
