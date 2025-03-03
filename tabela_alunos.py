import sqlite3

conexao = sqlite3.connect('banco')

comandos = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), 
# idade (inteiro) e curso (texto).

#comandos.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')


#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

# comandos.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Fabiana Hernande",32,"Engenharia de Dados")')
# comandos.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Beatriz Santos",29,"Psicologia")')
# comandos.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Maria Silva",19,"Recursos Humanos")')
# comandos.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Joana Magalhães",23,"Direito")')
# comandos.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Bianca Almeida",38,"Serviço Social")')
# comandos.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(6,"Janaina Andrade",27,"História")')
# comandos.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(7,"Carla Souza",20,"Letras")')
# comandos.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(8,"Marcia Ribeiro",31,"Engenharia de Produção")')

#3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".

# dados = comandos.execute('SELECT * FROM alunos')
# for alunos in dados:
#      print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

# dados_20 = comandos.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
# for alunos in dados_20:
#     print(alunos)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

# dados_engenharia = comandos.execute('SELECT * FROM alunos WHERE curso = "Engenharia de Dados" ORDER BY nome')
# for alunos in dados_engenharia:
#     print(alunos)

#d) Contar o número total de alunos na tabela

# dados_total = comandos.execute('SELECT COUNT(*) AS total_alunos FROM alunos')
# for alunos in dados_total:
#     print(alunos)

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.

#comandos.execute('UPDATE alunos SET idade=30 WHERE nome="Beatriz Santos"')

#b) Remova um aluno pelo seu ID.

# comandos.execute('DELETE FROM alunos WHERE ID=8')

#só é executado quando chegar nessa linha (se esquecer, não funciona)
conexao.commit()
# #encerrar a conexao (para não dar conflito)
conexao.close