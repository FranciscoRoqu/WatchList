def innerjoin_visualizadores_animes():
    from src.connection import cursor,close

    cur = cursor()

    cur.execute('''SELECT * FROM animes INNER JOIN visualizadores ON animes.id = visualizadores.id''')

    resultados = cur.fetchall()
    
    for vis_anime in resultados:
        print(vis_anime)

    close()