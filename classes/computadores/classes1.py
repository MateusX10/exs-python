class Computador:
    def __init__(self, marca, CPU, RAM, HD, GPU):
        self.marca = marca
        self.CPU = CPU
        self.RAM = RAM
        self.HD = HD
        self.GPU = GPU

    def Ligar(self):
        print('Estou ligando...')

    def Desligar(self):
        print('Estou desligando...')
    
    def ExibirInformacoesPc(self):
        print(f'MARCA: {self.marca}, CPU: {self.CPU}, RAM: {self.RAM}, HD: {self.HD}, GPU: {self.GPU}')

    @property
    def RAM(self):
        return self._RAM

    @RAM.setter
    def RAM(self, valor):
        self._RAM = valor.upper().replace('GB', 'KB')

    @property
    def HD(self):
        return self._HD

    @HD.setter
    def HD(self, valor):
        self._HD = valor.upper().replace("GB", "TB")

Computador1 = Computador("Acer", "pentium dual core", "3gb", "256GB", "INTEL FAMYLLIES")
Computador2 = Computador("DELL", "INTEL I5 8400", "14gb", "1TB", "RTX2070")
Computador3 = Computador("Acer", "intel i7 3770S", "6GB", "512GB", "GTX1070")

Computador1.Ligar()
Computador1.ExibirInformacoesPc()
Computador1.Desligar()
Computador2.Ligar()
Computador2.ExibirInformacoesPc()
Computador2.Desligar()
Computador3.Ligar()
Computador3.ExibirInformacoesPc()
Computador3.Desligar()