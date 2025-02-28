def insert_anime():
    """Insere um anime na base de dados"""
    from InquirerPy import inquirer
    from InquirerPy.validator import NumberValidator
    from InquirerPy.validator import EmptyInputValidator
    from src.connection import cursor,commit
    cur = cursor()
    cur.execute("SELECT COUNT(*) FROM visualizadores")
    resultados = cur.fetchone()
    if resultados[0] == 0:
        print("   É necessário existir pelo menu 1 visualizador para poder criar um anime")
        return
    
    nome = inquirer.text(message="Introduza o nome do anime: ",
                         validate=EmptyInputValidator(message="Por fazor introduza um valor")).execute()
    episodios = inquirer.text(message=f'Introduza o número de episódios que o anime "{nome}" tem: ', validate=NumberValidator(message="Por favor introduza um número")).execute()
    generos = []
    with open("generos.txt", "r") as ficheiro:
        generos_total = ficheiro.readline()
        generos = generos_total.split(",")
        if generos[len(generos) - 1] == "":
            generos.pop()
    genero = inquirer.fuzzy(
        message="Selecione os géneros do anime:",
        choices=generos,
        multiselect=True,
        validate=EmptyInputValidator,
        invalid_message="Por favor selecione um valor",
        instruction="Use as setas para navegar, TAB para selecionar e ENTER para confirmar."
    ).execute()
    genero_formatado = ""
    for valor in genero:
        genero_formatado = genero_formatado + valor + ", "
    genero_formatado = genero_formatado[:-2]

    cur.execute("SELECT id, nome_visualizador FROM visualizadores")
    visualizadores = cur.fetchall()
    escolhas = []
    for valor in visualizadores:
        visualizador_formatado = str(valor[0]) + "-> " + str(valor[1]) 
        escolhas.append(visualizador_formatado)
    visualizador = inquirer.select(message="Selecione o utilizador a quem deseja atribuir este anime: ",
                                   choices= escolhas,
                                   validate=EmptyInputValidator,
                                   invalid_message="Por favor selecione um valor").execute()
    visualizador_split = visualizador.split("-")
    cur.execute("INSERT INTO animes (anime, episodios, genero, ep_atual, visualizador) VALUES (?, ?, ?, 0, ?)", (nome, episodios, genero_formatado, visualizador_split[0]))

    commit()