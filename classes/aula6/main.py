from func import BaseDados

bd1 = BaseDados()

bd1.inserir_clientes("Fanis", 1)
bd1.inserir_clientes("prometheus", 2)
bd1.inserir_clientes("Zin", 3)
bd1.inserir_clientes("Ronaldo", 4)
bd1.inserir_clientes("Falcon", 5)
bd1.listar_clientes()
'''print(bd1._BaseDados__dados)
print(bd1.dados)'''
bd1._dados = "algo"
print(bd1._dados)
