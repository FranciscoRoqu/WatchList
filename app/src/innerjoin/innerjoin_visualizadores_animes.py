def innerjoin_visualizadores_animes():
    from src.connection import cursor

    cur = cursor()

    cur.execute('''SELECT * FROM visualizadores INNER JOIN animes ON visualizadores.id = animes.visualizador''')

    resultados = cur.fetchall()
    
    for vis_anime in resultados:
        print(vis_anime)