def read_animes():
    from src.connection import cursor,close

    cur = cursor()

    cur.execute('SELECT * FROM animes')

    resultados = cur.fetchall()
    
    for anime in resultados:
        print(anime)

    close()