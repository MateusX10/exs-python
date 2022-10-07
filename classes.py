import sys

class BichinhoVirtual:
    humor = 0
    def __init__(self, nome, idade, saude, cheio_de_comida):
        self.nome = nome
        self.idade = idade
        self.saude = saude
        self.cheio_de_comida = cheio_de_comida

    def MensagemDeErro(self):
        print("\033[1;31mTivemos um problema com o tipo de dados que você digitou\033[m")

    def MensagemDeErro2(self):
        print('\033[1;31mO usuário preferiu não informar os dados\033[m')


    def show_info_about(self):
        print(f'Nome: {self.nome} \nIdade: {self.idade} anos \nSaúde: {self.saude}% \nFome: {self.cheio_de_comida}%')

    def alterar_nome(self):
        novo_nome = str(input(f"Digite um novo nome (atual: {self.nome}): ")).strip().title()
        self.nome = novo_nome

    def alterar_idade(self):
        while True:
            nova_idade = str(input(f'Digite uma nova idade para {self.nome} (atual: {self.idade}): '))
            try:
                nova_idade = int(nova_idade)
            except (NameError, ValueError):
                MensagemDeErro()
            else:
                self.idade = nova_idade
                break
                
    def alterar_saude(self):
        while True:
            try:
                nova_saude = int(input(f"Digite a nova porcentagem de saúde para {self.nome} (atual: {self.saude}%): "))
            except (ValueError, NameError):
                MensagemDeErro()
            else:
                self.saude = nova_saude
                break


    def alterar_porcentagem_de_fome(self):
        nova_porcentagem_fome = int(input(f"Digite a nova porcentagem de saciação de {self.nome} (atual: {self.cheio_de_comida}%): "))
        if "%" in str(nova_porcentagem_fome):
            nova_porcentagem_fome.split("%")
            "".join(nova_porcentagem_fome)
        self.cheio_de_comida = nova_porcentagem_fome


    def BrincarComBichinho(self):
        while True:
            try:
                TempoDeBrincadeiraComBichinhos = int(input(f"Quanto tempo você pretende brincar com {self.nome} hoje? (em horas, de 0 a 24 horas): "))
            except (ValueError, NameError):
                MensagemDeErro()
            
            except (KeyboardInterrupt):
                MensagemDeErro2()
            else:
                break
        if (TempoDeBrincadeiraComBichinhos >= 4):
            self.saude = 100
        elif (TempoDeBrincadeiraComBichinhos >= 2):
            self.saude = 80
        elif (TempoDeBrincadeiraComBichinhos >= 1):
            self.saude = 60
        elif (TempoDeBrincadeiraComBichinhos == 0):
            self.saude = 20

    def AlimentarBichinho(self):
        while True:
            try:
                QuantidadeDeAlimentoDadoAoBichinho = int(input("Quantidade de alimento que você pretende dar ao bichinho (de 0 a 10): "))
            except(NameError, ValueError):
                MensagemDeErro()
            except(KeyboardInterrupt):
                MensagemDeErro2()
            else:
                break
                

        if QuantidadeDeAlimentoDadoAoBichinho >= 10:
            print(f'\033[1;31m{self.nome} não aguentou comer tanto e morreu, talvez vocẽ nunca mais devesse tentar ter um bichinho de novo...\033[m')
            self.cheio_de_comida = 1000
            exit()
        elif QuantidadeDeAlimentoDadoAoBichinho >= 8:
            print(f'\033[1;34m{self.nome} está muito bem alimentado, até demais...\033[m')
            self.cheio_de_comida = 100
        elif QuantidadeDeAlimentoDadoAoBichinho >= 5:
            print(f'\033[1;32m{self.nome} está cheio e feliz :)\033[m')
            self.cheio_de_comida = 100
        elif QuantidadeDeAlimentoDadoAoBichinho >= 3:
            print(f'\033[1;32m{self.nome} está satisfeito e feliz, olha que dono bom você é :)\033[m')
            self.cheio_de_comida = 100

        elif QuantidadeDeAlimentoDadoAoBichinho  >= 1:
            print(f'\033[1;33m{self.nome} está com um pouco de fome\033[m, \033[1;32mmas ele não reclamará, pois ama muito o seu dono :)\033[m')
            self.cheio_de_comida = 0
            self.saude = 0
        
        else:
            print(f'\033[1;31mEssa não!O que você fez?{self.nome.capitalize()} morreu de fome...\033[m')


    def calcular_humor(self):
        if (self.saude + self.cheio_de_comida) / 2 == 100:
            print(f'\033[1;32m{self.nome} está tão feliz que poderia morrer agora!!!\033[m')
        
        elif (self.saude + self.cheio_de_comida) / 2 >= 80:
            print(f'\033[1;32m{self.nome} está muito feliz!\033[m')

        elif (self.saude + self.cheio_de_comida) / 2 >= 60:
            print(f'\033[1;34m{self.nome} está feliz!\033[m ')

        elif (self.saude + self.cheio_de_comida) / 2 >= 40:
            print(f'\033[1;33m{self.nome} está triste :(\033[m')

        elif (self.saude + self.cheio_de_comida) / 2 >= 10:
            print(f'\033[1;31m{self.nome} está muito triste\033[m')

        else:
            print(f'\033[1;31m{self.nome} está morrendo...\033[m')

        
