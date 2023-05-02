class Heroi:
    '''
    Esta classe servirá como superclasse para as classes que represenram classes de herói, como mago,
    assasino, bruxa, etc...
    
    Atributos:

        nome (str): o nome do herói.
        dano (int): o dano que esse herói causa.
        defesa (int): a defesa desse herói.
        vida (int): os pontos de vida desse herói.
        ataque_especial: golpe especial do herói ("special move").
    '''

    def __init__(self, nome, dano, defesa,  vida, ataque_especial):
        '''
        O construtor da classe herói

        Parâmetros:

            nome (str): nome do herói
            dano (int): o dano que esse herói causa
            defesa (int): a defesa desse herói
            vida (int): os pontos de vida desse herói
            ataque_especial (int): ataque especial desse herói

            
        '''

        self.nome = nome
        self.dano = dano
        self.defesa = defesa
        self.vida = vida
        self.especial = ataque_especial

    

# Subclasse de "herói"    
class Mago(Heroi):
    '''
    Subclasse "mago" da classe "herói"

    Atributos:

        nome (str): nome do mago
        dano (int): dano que esse mago causa
        defesa (int): defesa que esse mago possui
        vida (int): os pontos de vida desse mago
        especial (int): o ataque especial desse mago ("special move")

    '''

    def __init__(self, nome):
        '''
        Construtor da classe "Mago".

        Parâmetros:

            nome (str): nome do mago
            dano (int): o dano que esse mago causa
            defesa (int): defesa do mago
            vida (int): pontos de vida do mago
            especial (int): golpe especial do mago ("special move")
        '''


        super().__init__(nome, dano=50, defesa=5, vida=1000, ataque_especial=300)


    




