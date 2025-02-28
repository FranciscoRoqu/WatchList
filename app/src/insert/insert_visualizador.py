def insert_visualizador():
    from InquirerPy import inquirer
    from InquirerPy.validator import NumberValidator
    from InquirerPy.validator import EmptyInputValidator
    from src.connection import cursor,commit
    cur = cursor()

    nome = inquirer.text(message="Introduza o nome do visualizador: ", validate=EmptyInputValidator(message="Por fazor introduza um valor")).execute()
    idade = inquirer.text(message=f'Introduza a idade do visualizador "{nome}": ', validate=NumberValidator(message="Por favor introduza um número")).execute()
    
    cur.execute("INSERT INTO visualizadores (nome_visualizador, idade_visualizador) VALUES (?, ?)", (nome, idade))

    commit()