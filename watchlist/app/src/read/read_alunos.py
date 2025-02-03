import sqlite3
 
 
conexao = sqlite3.connect('C:\\Users\\ba2442\\Documents\\psi\\DB_Management\\psi\\app\\sqlite-database\\epbjc.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM alunos')

resultados = cursor.fetchall()
 
for aluno in resultados:
    print(aluno)