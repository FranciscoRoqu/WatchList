def delete_animes():
    
    from InquirerPy import inquirer
    from InquirerPy.validator import NumberValidator
    from InquirerPy.validator import EmptyInputValidator
    from src.connection import cursor,commit,close
    cur = cursor()

    cur.execute("SELECT id, anime FROM animes")
    animes = cur.fetchall()
    animes_para_apagar = inquirer.fuzzy(
        message="Selecione os animes que deseja apagar: ",
        choices=animes,
        multiselect=True,
        validate=lambda resultado: len(resultado) >= 1,
        invalid_message="Por favor selecione um valor",
        instruction="Use as setas para navegar, TAB para selecionar e ENTER para confirmar."
    ).execute()

    commit()
    close()