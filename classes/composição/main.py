from classes import Cliente, Endereco

end1 = Endereco("SP", "SP")
c1 = Cliente("Mercs", 10)
c2 = Cliente("Martins", 49)
c3 = Cliente("Gob", 390)
c1.insere_endereco("Curitiba", "PE")
c1.insere_endereco("Maringá", "PR")
c2.insere_endereco("Florianópolis", "SC")
c3.insere_endereco("Rio de Janeiro", "RJ")
c1.lista_endereco()
c2.lista_endereco()
c3.lista_endereco()
