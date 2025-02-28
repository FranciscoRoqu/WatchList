def read_visualizadores():
    from src.connection import cursor

    cur = cursor()

    cur.execute('SELECT * FROM visualizadores')

    resultados = cur.fetchall()
    print("=" * 40)
    for visualizador in resultados:
            id, nome, idade = visualizador

            print(f"Nome: {nome}")
            print(f"ID: {id}")
            print(f"Idade: {idade}")
            print("=" * 40)  # Linha divisória para separar os visualizadores