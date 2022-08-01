class Livro:
    def __init__(self, titulo, paginas=None):
        self.titulo = titulo
        self.paginas = [] if not paginas else paginas
        self.pag_atual = 1

    def abrir(self):
        print('O livro foi aberto.')

    def fechar(self):
        print('O livro foi fechado.')

    def virar_frente(self, quant):
        if self.pag_atual + quant > self.paginas:
            print('\033[1;31mVocê já chegou ao fim do livro\033[m')
            return
        self.pag_atual += quant
        print(f'\033[1;32mLivro virado para a página {self.pag_atual} com sucesso!\033[m')

    def virar_tras(self, quant):
        if self.pag_atual - quant < 1:
            print('\033[1;31mERRO!Você não pode mais voltar páginas!\033[m')
            return
        self.pag_atual -= quant
        print(f'\033[1;32mLivro virado para a página {self.pag_atual} com sucesso!\033[m')

    @classmethod
    def set_pag(cls, titulo, paginas):
        return cls(titulo, paginas)