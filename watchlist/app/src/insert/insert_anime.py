def insert_anime():
    from InquirerPy import inquirer
    from InquirerPy.validator import NumberValidator
    from InquirerPy.validator import EmptyInputValidator
    from src.connection import cursor,commit,close
    cur = cursor()

    nome = inquirer.text(message="Introduza o nome do anime: ", validate=EmptyInputValidator(message="Por fazor introduza um valor")).execute()
    episodios = inquirer.text(message=f'Introduza o número de episódios que o anime "{nome}" tem: ', validate=NumberValidator(message="Por favor introduza um número")).execute()

    # cur.execute("INSERT INTO visualizadores (anime, episodios) VALUES (?, ?)", (nome, episodios))

    commit()
    close()