from api.omdb_api import get_movie
from schemas.movie import Movie


def main():
    while True:
        title: str = input("\nDigite o nome de um filme (ou 'sair'): ").strip()
        if title.lower() == 'sair':
            break

        movie: Movie = get_movie(title.replace(" ", "+"))

        if movie:
            print(movie)


if __name__ == "__main__":
    main()
