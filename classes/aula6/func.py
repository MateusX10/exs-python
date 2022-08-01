"""
Public, protected, private
"""
class BaseDados:
    def __init__(self):
        self._dados = {}

    '''@property
    def dados(self):
        return self._dados'''

    def inserir_clientes(self, nome, id):
        if "clientes" not in self._dados:
            self._dados["clientes"] = {id: nome}
        else:
            self._dados["clientes"].update({id: nome})

    def listar_clientes(self):
        for id, cliente in self._dados["clientes"].items():
            print(f'{id} = {cliente}')

    def apagar_cliente(self, id):
        del self._dados["clientes"][id]
