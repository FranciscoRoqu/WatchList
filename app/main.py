from src import *
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy.validator import EmptyInputValidator

generos = [
        "Romance",
        "Isekai",
        "Comédia",
        "Aventura",
        "Ação",
        "Drama",
        "Mecha",
        "Desporto",
        "Terror",
        "Fantasia",
        "Shounen",
        "Shoujo",
        "Seinen",
        "Josei",
        "Psicológico",
        "Sobrenatural",
        "Histórico",
        "Ecchi",
        "Harem",
        "Yuri",
        "Yaoi",
        "Música",
        "Gore",
        "Tragédia",
        "Sci-Fi",
        "Artes Marciais",
        "Paródia",
        "Militar",
        "Sobrevivência",
        "Mistério",
        "Escola",
        "Viagem no tempo"
    ]
generos.sort()
with open("generos.txt", "w") as ficheiro:
    for genero in generos:
        ficheiro.writelines(genero + ",")
def create_tabelas():
    """Criar as tabelas na base de dados"""
    create_animes()
    create_visualizadores()
create_tabelas()
while True:
    input = inquirer.select(message="Escolha um opção: ",
                            choices=[
                                "Inserir",
                                "Procurar",
                                "Atualizar",
                                "Apagar",
                                Separator(),
                                Choice(value=None,name="Sair")
                                ],
                                default="Inserir").execute()
    choices = ["Visualizador", 
               "Anime"]
    match input:
        case "Procurar" | "Apagar":
            choices.append("Tudo")
    if input is not None:
        answerInput = inquirer.select(message=f'O que deseja {input.lower()}:', 
                                      choices=choices,
                                      validate=EmptyInputValidator,
                                      invalid_message="Por favor selecione um valor",
                                      default=None).execute()
    match input:
        case "Inserir":
            match answerInput:
                case "Visualizador":
                    insert_visualizador()
                case "Anime":
                    insert_anime()
        case "Procurar":
            match answerInput:
                case "Visualizador":
                    read_visualizadores()
                case "Anime":
                    read_animes()
                case "Tudo":
                    innerjoin_visualizadores_animes()
        case "Apagar":
            match answerInput:  
                case "Visualizador":
                    delete_visualizadores()
                case "Anime":
                    delete_animes() 
                case "Tudo":
                    escolha = inquirer.select(message="Deseja realmente apagar todos os dados de todas as tabelas: ",
                                    choices=["Sim",
                                             "Não"],
                                    validate=EmptyInputValidator,
                                    invalid_message="Por favor selecione uma opção").execute
                    if escolha == "Sim":
                        drop_animes()
                        drop_visualizadores()
                        create_tabelas()
                    else:
                        print("Operação cancelada")
        case "Atualizar":
            match answerInput:  
                case "Visualizador":
                    update_visualizadores()
                case "Anime":
                    update_animes()
        case None:
            print("Saindo...")
            close()
            exit()