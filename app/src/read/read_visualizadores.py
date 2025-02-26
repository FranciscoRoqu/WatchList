def read_visualizadores():
    from src.connection import cursor

    cur = cursor()

    cur.execute('SELECT * FROM visualizadores')

    resultados = cur.fetchall()
    
    for visualizador in resultados:
        print(visualizador)