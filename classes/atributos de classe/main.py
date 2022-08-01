from classes import Celular

cel1 = Celular()
cel2 = Celular()

cel1.id = 000
Celular.id = 999
print(cel1.id)
print(cel2.id)
print(cel1.marca)
print(cel2.marca)
print(Celular.id)
print(cel1.__dict__)
print(cel2.__dict__)
print(Celular.__dict__)
