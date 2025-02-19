def create_animes():
    
    from src.connection import cursor,commit,close
    
    cur = cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS animes(
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            anime     TEXT    NOT NULL,
            episodios INTEGER NOT NULL,
            genero    TEXT    NOT NULL
    )
    ''')
    
    commit()
    close()