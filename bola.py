class Bola:
    cores = ["azul", "amarelo", "vermelho", "marrom", "cinza",
                 "verde", "azul escuro", "azul claro", "ciano", "lilás",
                 "preto", "branco", "roxo", "violeta", "bege"]
    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor

    @property
    def circunferencia(self):
        return self.__circunferencia

    @circunferencia.setter
    def circunferencia(self, nova_circunferencia):
        self.__circunferencia = nova_circunferencia

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, novo_material):
        self.__material = novo_material

    def show_info_about(self):
        print(f'''Cor da bola: {self.__cor} \n Circunferência: {self.__circunferencia} cm
Material: {self.__material}''')

    
    def trocar_cor(self):
        while True:
            try:
                nova_cor = str(input(f"\033[1mDigite a nova cor para a bola: (atual: {self.cor})")).lower().strip()
            except (KeyboardInterrupt):
                print("\n\033[1;31mO usuário preferiu não informar os dados.\033[m")
                break
            else:
                if nova_cor in self.cores:
                    print(f'Cor atualizada de {self.cor} para {nova_cor} com sucesso!\033[m')
                    self.cor = nova_cor
                    break
                else:
                    print("\033[1;31mCor inválida!Tente novamente...\033[m")
            
    def mostrar_cor(self):
        print(f'Cor atual: {self.__cor}')




bola1 = Bola("azul", 10.5, "couro")

bola1.show_info_about()

bola1.trocar_cor()
bola1.show_info_about()
bola1.mostrar_cor()