from composicao import Cliente, Endereco

cliente1 = Cliente("Fernando", 20)
cliente1.inserir_endereco("BELO HORIZONTE", "MG")
print(cliente1.nome)
cliente1.listar_enderecos()
del cliente1

cliente2 = Cliente("Maria", 40)
cliente2.inserir_endereco("Florianópolis", "SC")
cliente2.inserir_endereco("SP", "SP")
print(cliente2.nome)
cliente2.listar_enderecos()
del cliente2

cliente3 = Cliente("Mateus", 30)
cliente3.inserir_endereco("MARINGÁ", "PR")
print(cliente3.nome)
cliente3.listar_enderecos()
del cliente3

print('\033[1;34m&&&&&&&&&&&&&&&&&&&&&&&&&&')

