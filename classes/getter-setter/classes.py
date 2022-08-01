class Conta:
    def __init__(self, nome_conta, saldo):
        self.nome = nome_conta
        self.saldo = saldo
        self._reserva = 0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, str):
            valor = valor.replace("R$", "")
            valor = float(valor.replace(",", "."))
        if(valor < 0):
            print('\033[1;31mSaldo não pode ser negativo\033[m')
            print('<<< O saldo foi redefinido para 0 >>>')
            valor = 0
        self._saldo = valor


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        novo_nome = ''
        if isinstance(valor, int):
            print('\033[1;31mNome da conta não pode ser um número\033[m')
            while True:
                novo_nome = str(input('Digite um novo nome para a conta: '))
                if novo_nome.isalpha():
                    valor = novo_nome
                    print(f'\033[1;32mNovo nome da conta definido para {valor} com sucesso!\033[m')
                    break
                print('\033[1;31mDigite um nome válido!\033[m')

        self._nome = valor

    @property
    def reserva(self):
        return self._reserva

    @reserva.setter
    def reserva(self, novo):
        novo += 30500
        self._reserva = novo
    

    

    def VerSituacaoDaConta(self):
        print(f'''Nome da conta: {self.nome}
Saldo: R${self.saldo:.2f}''')


    def emprestimo(self, quantia):
        juros = quantia + (quantia * 30 / 100)
        print(f'\033[1;32mVocê está emprestando R${quantia} de nosso banco')
        print(f'Tenha em mente que você deverá pagar R${juros:.2f} para o banco até 30 dias após o empréstimo bancário\033[m')
        self.saldo += quantia
