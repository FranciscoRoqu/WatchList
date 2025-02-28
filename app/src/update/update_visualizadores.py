def update_visualizadores():
    from InquirerPy import inquirer
    from InquirerPy.validator import NumberValidator
    from InquirerPy.validator import EmptyInputValidator
    from src.connection import cursor,commit
    cur = cursor()

    vis_atual = inquirer.select(message="Escolha o visualizador que deseja atualizar: ",
                                choices=[row[1] for row in cur.execute("SELECT * FROM visualizadores")],
                                validate=EmptyInputValidator,
                                invalid_message="Por favor selecione uma opção").execute()
    
    cur.execute("SELECT * FROM visualizadores WHERE nome_visualizador = '" + vis_atual + "'")
    vis_atual = cur.fetchone()

    if vis_atual is None:
        print("Não foi encontrado nenhum visualizador com esse nome.")
        return

    novo_nome = inquirer.text(message="Introduza o novo nome do utilizador: ",
                              default=vis_atual[1]).execute()

    nova_idade = inquirer.text(message="Introduza a nova idade do utilizador: ",
                               default=str(vis_atual[2]), validate=NumberValidator()).execute()

    cur.execute("UPDATE visualizadores SET nome_visualizador = ?, idade_visualizador = ? WHERE id = ?", (novo_nome, nova_idade, vis_atual[0]))

    commit()