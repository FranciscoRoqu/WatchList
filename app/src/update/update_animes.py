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

    escolha = inquirer.select(message="Deseja realmente alterar os dados do anime ?: ",
                              choices=["Sim",
                                       "Não"],
                              validate=EmptyInputValidator,
                              invalid_message="Por favor selecione uma opção").execute()
    if escolha == "Sim":
        cur.execute("UPDATE animes SET anime = ?, episodios = ? WHERE id = ?", (novo_nome, novos_episodios, anime_atual[0]))
    else:
        print("Operação cancelada")
    commit()