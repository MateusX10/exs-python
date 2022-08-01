'''Public, protected, private'''

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, nome, id):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}
        else:
            self.__dados["clientes"].update({id: nome})

    def lista_clientes(self):
        print('\033[1;34m === Lista de clientes: === \033[m')
        for k, cliente in self.__dados["clientes"].items():
            print(f'Nome: {cliente}, ID: {k}')

    def apaga_cliente(self, id):
        cliente_apagado = self.__dados["clientes"][id]
        try:
            del self.__dados["clientes"][id]
        except:
            print(f'\033[1;31mNão foi possível apagar o cliente {self.dados["clientes"][id]}\033[m')
        else:
            print(f'\033[1;32mCliente {cliente_apagado} apagado com sucesso\033[m')

        