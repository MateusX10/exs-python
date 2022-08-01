class Leao:
    def __init__(self, cor, alt):
        self.__cor = None
        self.__alt = alt

    @property
    def alt(self):
        return self.__alt

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, valor):
        self.__cor = valor

class Elefante:
    def __init__(self, cor, alt):
        self.__cor = cor
        self.__alt = alt

    @property
    def cor(self):
        return self.__cor
    @property
    def alt(self):
        return self.__alt