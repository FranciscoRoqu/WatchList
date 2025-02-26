def delete_visualizadores():
    from InquirerPy import inquirer
    from InquirerPy.validator import NumberValidator
    from InquirerPy.validator import EmptyInputValidator
    from src.connection import cursor,commit
    cur = cursor()

    cur.execute("SELECT id, nome_visualizador FROM visualizadores")
    visualizadores = cur.fetchall()

    escolhas = []
    for valor in visualizadores:
        anime_formatado = str(valor[0]) + "-> " + str(valor[1]) 
        escolhas.append(anime_formatado)
    visualizadores_para_apagar = inquirer.fuzzy(
        message="Selecione os visualizadores que deseja apagar: ",
        choices=escolhas,
        multiselect=True,
        validate=lambda resultado: len(resultado) >= 1,
        invalid_message="Por favor selecione um valor",
        instruction="Use as setas para navegar, TAB para selecionar e ENTER para confirmar."
    ).execute()
    i = 0
    for valor in visualizadores_para_apagar:
        visualizador = valor[i]
        visualizador_split = visualizador.split("-")
        cur.execute('DELETE FROM visualizadores WHERE id=' + visualizador_split[0])
    commit()