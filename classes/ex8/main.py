class Celular:
    def __init__(self, marca, processador, ram, flash):
        self.marca = marca
        self.processador = processador
        self.ram = ram
        self.flash = flash

cel1 = Celular("asus", "Snapdragon 855", "10gb", "128GB")
print(cel1.marca,cel1.processador,  cel1.ram, cel1.flash)