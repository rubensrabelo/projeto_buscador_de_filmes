from api.omdb_api import get_movie, search_movies_by_keyword
from schemas.movie import Movie


def main() -> None:
    while True:
        print("\nEscolha: \n[1] Buscar por título\n[2] Buscar por palavra-chave\n[3] Sair: ")
        opcao = input("Digite aqui: ")

        if opcao == "1":
            title = input("Digite o título do filme: ").strip()
            movie = get_movie(title)
            if movie:
                print(movie)

        elif opcao == "2":
            keyword = input("Digite uma palavra-chave: ").strip()
            movies = search_movies_by_keyword(keyword)
            if movies:
                for m in movies:
                    print(m)
        
        elif opcao == "3":
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
