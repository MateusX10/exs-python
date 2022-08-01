from numeros import *
from datetime import datetime

class Cliente:
    atual = datetime.today().year
    def __init__(self):
        self.nome = self.AnoNasc = self.MesNasc = self.DiaNasc = self.email = self.senha = self.numero = None

    def ExibirInfoCliente(self):
        senha_escondida = self.senha
        temp = ""
        while True:
            escolha = str(input('Mostrar a senha? [S/N]')).strip().upper()[0]
            if escolha in "SN":
                break
            print('\033[1;31mDigite somente "S" ou "N"\033[m')
        if escolha == "N":
            for caracter in range(0, len(senha_escondida)):
                temp += "*"
            senha_escondida = temp

        print(f'''\n\033[1;34m=== Informações da Conta: ===\033[0m \033[1m
==> Nome: {self.nome}
==> Data de nascimento: {self.DiaNasc}/{self.MesNasc}/{self.AnoNasc}
==> E-mail: {self.email}
==> Senha: {senha_escondida}
==> Número de telefone: +55 (41) 9 {self.numero}
\033[m''')

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo):
        while True:
            novo = str(input('Nome: ')).title()
            if len(novo) >= 3:
                break
            print('\033[1;31mERRO!Digiteu nome válido!\033[m')
        self._nome = novo

    @property
    def AnoNasc(self):
        return self._AnoNasc

    @AnoNasc.setter
    def AnoNasc(self, novo_ano):
        while True:
            novo_ano = leiaInt("Ano nascimento: ")
            if novo_ano < 1900 or novo_ano > self.atual:
                print('\033[1;31mAno de nascimento impossível.Tente novamente\033[m')
                continue
            break
        self._AnoNasc = novo_ano

    @property
    def MesNasc(self):
        return self._MesNasc

    @MesNasc.setter
    def MesNasc(self, novo_mes):
        while True:
            novo_mes = leiaInt("Mês de nascimento: ")
            if 0 < novo_mes < 13:
                if novo_mes < 10:
                    novo_mes = ZeroaEsquerda(novo_mes)
                break
            print('\033[1;31mMês de nascimento impossível.Tente novamente\033[m')
        self._MesNasc = novo_mes

    @property
    def DiaNasc(self):
        return self._DiaNasc

    @DiaNasc.setter
    def DiaNasc(self, novo_dia):
        while True:
            novo_dia = leiaInt("Dia de nascimento: ")
            if 0 < novo_dia < 32:
                if novo_dia < 10:
                    novo_dia = ZeroaEsquerda(novo_dia)
                break
            print('\033[1;31mDia de nascimento impossível.Tente novamente\033[m')
        self._DiaNasc = novo_dia

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        while True:
            novo_email = str(input('E-mail: ')).strip().replace("@gmail.com", "")
            if 5 < len(novo_email) < 31:
                novo_email += "@gmail.com"
                break
            print('\033[1;31mSeu e-mail deve ter entre 6 a 30 caracteres\033[m')
        self._email = novo_email

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        numeros = ["1","2","3","4","5","6","7","8","9"]
        letras = ["a", "b", "c", "d", "e", "f", "g", "h",
                 "i", "j", "k", "l", "m", "n", "o", "p",
                 "q", "r", "s", "t", "u", "v", "w", "x",
                 "y", "z"]
        quant_num = quant_letra = 0 #variável para verificar se há números na senha e se há letras na senha, respectivamentes
        while True:
            nova_senha = str(input('Senha: (\033[1mUSAR 8 CARACTERES OU MAIS COM SÍMBOLOS E NÚMEROS)'))
            if len(nova_senha) > 7:
                for n in numeros:
                    if n in nova_senha:
                        quant_num += 1
                for l in letras:
                    if l in nova_senha or l.upper() in nova_senha:
                        quant_letra += 1
                if quant_num > 0 and quant_letra > 0:
                    break
            print('\033[1;31mUse uma senha mais segura!\033[m')
        self._senha = nova_senha

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, novo_numero):
        copy = ""
        while True:
            novo_numero = str(leiaInt("Número de telefone: +55 (41) 9 "))
            if len(novo_numero) == 8:
                for n in range(0, len(str(novo_numero))):
                    if n == 4:
                        copy += "-"
                    copy += novo_numero[n]
                novo_numero = copy
                break
            print('\033[1;31mDigite um número de telefone válido!\033[m')

        self._numero = novo_numero
        

    





    





  


    
