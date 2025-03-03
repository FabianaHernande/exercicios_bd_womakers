import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('banco')
comandos = conexao.cursor()

# Criar a tabela "compras"
# comandos.execute('''
#     CREATE TABLE IF NOT EXISTS compras (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         cliente_id INTEGER,
#         produto TEXT NOT NULL,
#         valor REAL NOT NULL,
#         FOREIGN KEY (cliente_id) REFERENCES clientes(id)
#     )
# ''')

# # Inserir registros na tabela "compras"
# comandos.executemany('''
#     INSERT INTO compras (cliente_id, produto, valor) VALUES (?, ?, ?)
# ''', [
#     (1, 'Notebook', 4500.00),
#     (2, 'Smartphone', 2500.00),
#     (3, 'Geladeira', 3500.00),
#     (4, 'Fone de Ouvido', 200.00),
#     (5, 'TV 55 Polegadas', 4000.00),
#     (1, 'Teclado Mecânico', 350.00),
#     (3, 'Cadeira Gamer', 1200.00)
# ])

# # Salvar as alterações
conexao.commit()

# # Consultar nome do cliente, produto e valor da compra
# comandos.execute('''
#     SELECT clientes.nome, compras.produto, compras.valor
#     FROM compras
#     JOIN clientes ON compras.cliente_id = clientes.id
# ''')

# # Exibir os resultados
# for linha in comandos.fetchall():
#     print(linha)

# # Fechar conexão
conexao.close()