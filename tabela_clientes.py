import sqlite3

conexao = sqlite3.connect('banco')

comandos = conexao.cursor()

#5. Criar uma Tabela e Inserir Dados
# Crie uma tabela chamada "clientes" com os campos: id (chave primária), 
# nome (texto), idade (inteiro) e saldo (float). Insira alguns
# registros de clientes na tabela.

# comandos.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo float)')

# comandos.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(1,"Fabiana Hernande",32,5305.00)')
# comandos.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(2,"Beatriz Santos",29,3850.00)')
# comandos.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(3,"Maria Silva",19,2800.00)')
# comandos.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(4,"Joana Magalhães", 23,4890.00)')
# comandos.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(5,"Bianca Almeida", 38,2350.00)')
# comandos.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(6,"Janaina Andrade", 27,2150.00)')
# comandos.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(7,"Carla Souza",20, 2150.00)')
# comandos.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(8,"Marcia Ribeiro", 31,3475.00)')

#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

# dados_30 = comandos.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
# for clientes in dados_30:
#     print(clientes)

#b) Calcule o saldo médio dos clientes.

# dados_saldo = comandos.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')
# for clientes in dados_saldo:
#     print(clientes)

#c) Encontre o cliente com o saldo máximo

# dados_saldo_max = comandos.execute('SELECT nome, saldo  FROM clientes ORDER BY saldo DESC LIMIT 1')
# for clientes in dados_saldo_max:
#     print(clientes)

#d) Conte quantos clientes têm saldo acima de 1000.

# dados_saldo_acima = comandos.execute('SELECT COUNT(*) AS total_clientes FROM clientes WHERE saldo > 1000')
# for clientes in dados_saldo_acima:
#     print(clientes)

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.

# comandos.execute('UPDATE clientes SET saldo=4330.00 WHERE nome="Beatriz Santos"')

#b) Remova um cliente pelo seu ID.

# comandos.execute('DELETE FROM clientes WHERE ID=5')

#só é executado quando chegar nessa linha (se esquecer, não funciona)
conexao.commit()
# #encerrar a conexao (para não dar conflito)
conexao.close