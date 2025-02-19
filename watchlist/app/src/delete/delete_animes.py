def delete_animes():
    
    from InquirerPy import inquirer
    from InquirerPy.validator import NumberValidator
    from InquirerPy.validator import EmptyInputValidator
    from src.connection import cursor,commit,close
    cur = cursor()

    nome = inquirer.text(message="Introduza o nome do anime: ", validate=EmptyInputValidator(message="Por fazor introduza um valor")).execute()
    cur.execute("DELETE FROM animes WHERE anime = ?", (nome))

    commit()
    close()