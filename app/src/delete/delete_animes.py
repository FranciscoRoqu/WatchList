def delete_animes():
    from InquirerPy import inquirer
    from InquirerPy.validator import NumberValidator
    from InquirerPy.validator import EmptyInputValidator
    from src.connection import cursor,commit
    cur = cursor()

    cur.execute("SELECT id, anime FROM animes")
    animes = cur.fetchall()

    escolhas = []
    for valor in animes:
        anime_formatado = str(valor[0]) + "-> " + str(valor[1]) 
        escolhas.append(anime_formatado)
    animes_para_apagar = inquirer.fuzzy(
        message="Selecione os animes que deseja apagar: ",
        choices=escolhas,
        multiselect=True,
        validate=lambda resultado: len(resultado) >= 1,
        invalid_message="Por favor selecione um valor",
        instruction="Use as setas para navegar, TAB para selecionar e ENTER para confirmar."
    ).execute()
    i = 0
    for valor in animes_para_apagar:
        anime = valor[i]
        anime_split = anime.split("-")
        cur.execute('DELETE FROM animes WHERE id=' + anime_split[0])
    commit()