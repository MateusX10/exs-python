class Frase:
    def __init__(self, frase):
        self.frase = frase
    
    @property
    def frase(self):
        return self._frase

    @frase.setter
    def frase(self, valor):
        valor = valor.split()
        self._frase = valor[0]

f = str(input('Digite uma palavra (não nos responsabilizamos por frases cortadas): '))
frase1 = Frase(f)    

print(frase1.frase)
