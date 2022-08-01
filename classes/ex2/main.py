from quadrado import Quadrado

quad1 = Quadrado(18)
quad2 = Quadrado(20)
quad3 = Quadrado(8)

print(quad1.tamanho_lado, quad2.tamanho_lado, quad3.tamanho_lado)
quad1.MostrarValorLado()
quad1.MudarValorLado()
quad1.MostrarValorLado()
print(quad1.Area())
print(quad2.Area())
print(quad3.Area())