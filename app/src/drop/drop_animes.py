def drop_animes():
    
    from src.connection import cursor,commit,close
    cur = cursor()

    cur.execute("DROP TABLE animes")

    commit()
    close()