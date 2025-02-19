def create_visualizadores():
    
    from src.connection import cursor,commit,close
    cur = cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS visualizadores (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_visualizador   TEXT    NOT NULL,
            idade_visualizador  INTEGER NOT NULL,
            
            FOREIGN KEY (id)    REFERENCES animes (id)
        )
    ''')
    
    commit()
    close()