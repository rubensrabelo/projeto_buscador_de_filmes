from api.omdb_api import get_movie


def main():
    while True:
        title = input("\nDigite o nome de um filme (ou 'sair'): ").strip()
        if title.lower() == 'sair':
            break

        movie = get_movie(title.replace(" ", "+"))

        if movie:
            print(movie)


if __name__ == "__main__":
    main()
