def insert_anime():
    from InquirerPy import inquirer
    from InquirerPy.validator import NumberValidator
    from InquirerPy.validator import EmptyInputValidator
    from src.connection import cursor,commit,close
    cur = cursor()

    nome = inquirer.text(message="Introduza o nome do anime: ", validate=EmptyInputValidator(message="Por fazor introduza um valor")).execute()
    episodios = inquirer.text(message=f'Introduza o número de episódios que o anime "{nome}" tem: ', validate=NumberValidator(message="Por favor introduza um número")).execute()
    generos = [
        "Romance",
        "Isekai",
        "Comédia",
        "Aventura",
        "Ação",
        "Drama",
        "Mecha",
        "Desporto",
        "Terror",
        "Fantasia",
        "Shounen",
        "Shoujo",
        "Seinen",
        "Josei",
        "Psicológico",
        "Sobrenatural",
        "Histórico",
        "Ecchi",
        "Harem",
        "Yuri",
        "Yaoi",
        "Música",
        "Gore",
        "Tragédia",
        "Sci-Fi",
        "Artes Marciais",
        "Paródia",
        "Militar",
        "Sobrevivência",
        "Mistério",
        "Escola",
        "Viagem no tempo"
    ]
    generos.sort()
    genero = inquirer.fuzzy(
        message="Selecione os géneros do anime:",
        choices=generos,
        multiselect=True,
        validate=lambda resultado: len(resultado) >= 1,
        invalid_message="Por favor selecione um valor",
        instruction="Use as setas para navegar, TAB para selecionar e ENTER para confirmar."
    ).execute()
    genero_formatado = ""
    for valor in genero:
        genero_formatado = genero_formatado + valor + ", "
    genero_formatado = genero_formatado[:-2]
    cur.execute("INSERT INTO animes (anime, episodios, genero, ep_atual) VALUES (?, ?, ?, 0)", (nome, episodios, genero_formatado))

    commit()
    close()