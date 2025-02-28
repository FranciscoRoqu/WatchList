def create_visualizadores():
    """Cria a tabela de visualizadores"""
    from src.connection import cursor,commit
    cur = cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS visualizadores (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_visualizador   TEXT    NOT NULL,
            idade_visualizador  INTEGER NOT NULL
        )
    ''')
    
    commit()