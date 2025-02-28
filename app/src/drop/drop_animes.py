def drop_animes():
    from src.connection import cursor,commit

    cur = cursor()
    print("A apagar a tabela 'animes'")
    cur.execute("DROP TABLE animes")

    commit()