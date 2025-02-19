def read_visualizadores():
    from src.connection import cursor,close

    cur = cursor()

    cur.execute('SELECT * FROM visualizadores')

    resultados = cur.fetchall()
    
    for visualizador in resultados:
        print(visualizador)

    close()


read_visualizadores()