from classes import BaseDeDados

bd1 = BaseDeDados()
bd1.__dados = "você foi hackeado"
bd1.inserir_cliente("Fernando", 1)
bd1.inserir_cliente("Maurício", 2)
bd1.inserir_cliente("Souza", 3)
bd1.apaga_cliente(3)

print(bd1._BaseDeDados__dados)
print(bd1.dados)
bd1.lista_clientes()
