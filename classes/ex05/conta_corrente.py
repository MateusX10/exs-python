class ContaCorrente:
    def __init__(self, nome_conta, nome_correntista, saldo):
        self.nome_conta = nome_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def AltNome(self, novo="dívida"):
        self.nome_conta = novo
    
    def VerDepósito(self):
        print(f'Você tem ao todo R${self.saldo:.2f} na conta')
        while True:
            escolha = str(input('Deseja sacar algum valor? [S/N]')).strip().upper()[0]
            if escolha in "SN":
                break
            print('\033[1;31mERRO!Digite uma opção válida!\033[m')
        return escolha

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))
        self._saldo = valor


    def Sacar(self, quant):
        if self.saldo >= quant:
            self.saldo -= quant
        else:
            print(f'\033[1;31mSó foi possível sacar R${self.saldo:.2f}, pois é o que você tem ._.\033[m')
            self.saldo = 0
            return
        print(f'Você sacou R${quant:.2f} de sua conta bancária')    
    