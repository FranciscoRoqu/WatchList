def update_animes():

    from InquirerPy import inquirer
    from InquirerPy.validator import NumberValidator
    from InquirerPy.validator import EmptyInputValidator
    from src.connection import cursor,commit
    cur = cursor()

    anime_atual = inquirer.select(message="Escolha o anime que deseja atualizar: ",
                                choices=[row[1] for row in cur.execute("SELECT * FROM animes")],
                                validate=EmptyInputValidator,
                                invalid_message="Por favor selecione um anime").execute()

    cur.execute("SELECT * FROM animes WHERE anime = '" + anime_atual + "'")
    anime_atual = cur.fetchone()

    if anime_atual is None:
        print("Não foi encontrado nenhum anime com esse nome.")
        return
    novo_nome = inquirer.text(message="Introduza o novo nome do anime: ",
                              default=anime_atual[1]).execute()

    novos_episodios = inquirer.text(message="Introduza o novo número de episódios: ",
                                    default=str(anime_atual[2]),
                                    validate=NumberValidator()).execute()

    generos = []
    with open("generos.txt", "r") as ficheiro:
        generos_total = ficheiro.readline()
        generos = generos_total.split(",")
        if generos[len(generos) - 1] == "":
            generos.pop()

    novos_generos = inquirer.fuzzy(
        message="Selecione os novos géneros do anime:",
        choices=generos,
        multiselect=True,
        validate=EmptyInputValidator,
        invalid_message="Por favor selecione um valor",
        instruction="Use as setas para navegar, TAB para selecionar e ENTER para confirmar."
    ).execute()

    genero_formatado = ""
    for valor in novos_generos:
        genero_formatado = genero_formatado + valor + ", "
    novo_genero_formatado = genero_formatado[:-2]
    cur.execute("SELECT id, nome_visualizador FROM visualizadores")

    visualizadores = cur.fetchall()
    escolhas = []
    for valor in visualizadores:
        visualizador_formatado = str(valor[0]) + "-> " + str(valor[1])
        escolhas.append(visualizador_formatado)
    novo_visualizador = inquirer.select(message="Selecione o novo visualizador a quem atribuir este anime: ",
                                        choices = escolhas,
                                        validate=EmptyInputValidator,
                                        invalid_message="Por favor selecione um valor").execute()
    visualizador_split = novo_visualizador.split(">")
    novo_episodio_atual = inquirer.text(message="Em que episódio de " + novo_nome + " está o" + visualizador_split[1] + ":",
                                        validate=NumberValidator,
                                        invalid_message="Por favor digite um número").execute()

    escolha = inquirer.select(message="Deseja realmente alterar os dados do anime ?: ",
                              choices=["Sim",
                                       "Não"],
                              validate=EmptyInputValidator,
                              invalid_message="Por favor selecione uma opção").execute()

    if escolha == "Sim":
        cur.execute("UPDATE animes SET anime = ?, "
                    "episodios = ?, "
                    "genero = ?, "
                    "ep_atual = ?, "
                    "visualizador = ? "
                    "WHERE id = ?",
                    (novo_nome,
                     novos_episodios,
                     novo_genero_formatado,
                     novo_episodio_atual,
                     visualizador_split[0][:-1],
                     anime_atual[0]))
    else:
        print("Operação cancelada")
    commit()