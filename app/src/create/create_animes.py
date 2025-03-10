def create_animes():
    """Cria a tabela de animes"""
    from src.connection import cursor,commit
    
    cur = cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS animes(
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            anime        TEXT    NOT NULL,
            episodios    INTEGER NOT NULL,
            genero       TEXT    NOT NULL,
            ep_atual     INTEGER NOT NULL,
            visualizador INTEGER NOT NULL,
                
            FOREIGN KEY (visualizador) REFERENCES visualizadores(id)
    )
    ''')
    
    commit()