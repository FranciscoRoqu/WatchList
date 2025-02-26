def drop_visualizadores():
    
    from src.connection import cursor,commit,close
    cur = cursor()

    cur.execute("DROP TABLE visualizadores")

    commit()
    close()