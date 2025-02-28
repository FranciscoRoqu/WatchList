def drop_visualizadores():
    
    from src.connection import cursor,commit
    cur = cursor()
    print("A apagar a tabela 'visualizadores'")
    cur.execute("DROP TABLE visualizadores")

    commit()