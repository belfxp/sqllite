import sqlite3#ele importa o sqlite

banco = sqlite3.connect('banco de dados.db')#ele cria um bd

cursor = banco.cursor()#cria um objeto que vai receber o bd criado

cursor.execute("CREATE TABLE professor (matricula integer, nome text, materia text)")#ele cria uma tabela

cursor.execute("INSERT INTO professor VALUES(3, 'Diego', 'programacao')")#ele adicionar valores a tabela

banco.commit()#confirma as mudanças na tabela

cursor.execute("SELECT * FROM professor")#seleciona o que vai printar da tabela
print(cursor.fetchall())#printa a tabela
