class Internet:
    def __init__(self, nome_rede, endereco_ip, frequencia):
        self.nome_rede = nome_rede
        self.endereco_ip = endereco_ip
        self.frequencia = frequencia

    def ExibirInfos(self):
        print(f'''Nome da rede: {self.nome_rede}
Endereço de IP: {self.endereco_ip}
Frequência: {self.frequencia}''')

    @staticmethod
    def usuario():
        print('Apenas um usuário pouco anônimo')

    @staticmethod
    def anônimo():
        print('Apenas um usuário anônimo')

    @staticmethod
    def hacker():
        print('Apenas um usuário hacker comum')

    