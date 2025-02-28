def read_animes():
    from src.connection import cursor

    cur = cursor()

    cur.execute('SELECT * FROM animes')
    resultados = cur.fetchall()
    if not resultados:
        print("Não existem animes na base de dados")
        return
    print("=" * 40)
    for anime in resultados:
        id, nome, episodios, generos, episodio_atual, id_visualizador = anime

        print(f"Anime: {nome}")
        print(f"ID: {id}")
        print(f"Episódios Totais: {episodios}")
        print(f"Géneros: {generos}")
        print(f"Episódio Atual: {episodio_atual}")
        print(f"ID do Visualizador: {id_visualizador}")
        print("=" * 40)  # Linha divisória para separar os animes