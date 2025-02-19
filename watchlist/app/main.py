from src import *
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

input = inquirer.select(message="Escolha um opção: ",
                        choices=[
                            "Inserir",
                            "Procurar",
                            "Atualizar",
                            "Apagar",
                            Separator(),
                            Choice(value=None,name="Sair")
                            ],
                            default=None).execute()
choices = ["Visualizador", 
           "Anime"]
match input:
    case "Procurar" | "Apagar":
        choices.append("Tudo")
if input != None:
    answerInput = inquirer.select(message=f'O que deseja {input}:', 
                                  choices=choices, 
                                  default=None).execute()
match input:
    case "Inserir":
        create_visualizadores()
        create_animes()
        match answerInput:
            case "Visualizador":
                insert_visualizador()
            case "Anime":
                insert_anime()
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
                delete_visualizadores()
                delete_animes() 
    case "Atualizar":
        match answerInput:  
            case "Visualizador":
                update_visualizadores()
            case "Anime":
                update_animes()

    case None:
        print("Saindo...")
        exit()