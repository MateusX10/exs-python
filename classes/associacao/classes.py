class Computador:
    def __init__(self, nome, marca, quant_ram, cpu, hd):
        self.nome = nome
        self.marca = marca
        self.quant_ram = quant_ram
        self.cpu = cpu
        self.hd = hd
        self.inserir_dado = self.selecionar_dado = None

    def ExibirFicha(self):
        print(f'''FICHA TÉCNICA DO PC:
Marca: {self.marca}
RAM: {self.quant_ram}
CPU: {self.cpu}
HD: {self.hd}''')


class Teclado:
    def __init__(self):
        self.algo = "alguma coisa"

    def digitar(self):
        print('Digitação iniciada...')

    def backspace(self):
        print('Deletação iniciada...')

    def space(self):
        print('Espaçamento entre palavras iniciado...')

    

    
class Mouse:
    def __init__(self):
        pass

    def clicar(self):
        print('Clicação iniciada...')

    def rolar(self):
        print('Rolação entre objetos iniciada...')

    def botao_direito(self):
        print('Botão direito pressionado, opções a amostra...')