class Pc:
    def __init__(self):
        self.comandos = []

    def digitar_comando(self, comando):
        self.comandos.append(comando)

    def listar_comandos(self):
        for comando in self.comandos:
            print(comando.comando)

    def comandos_tot(self):
        print(f'Número de comandos efetuados: {len(self.comandos)}')

class Teclado:
    def __init__(self, comando):
        self.comando = comando

class Mouse:
    def __init__(self, comando):
        self.comando = comando