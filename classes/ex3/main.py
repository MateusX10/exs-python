from retangulo import Retangulo

ret1 = Retangulo(10, 12)
ret2 = Retangulo(14, 20)

print(ret1.comprimento, ret1.largura)
print(ret2.comprimento, ret2.largura)

print(ret1.MostrarLados(), ret2.MostrarLados())
ret1.MudarLados()
ret2.MudarLados()
print(ret1.MostrarLados(), ret2.MostrarLados())
print(f'Área: {ret1.area()} cm², {ret2.area()} cm²')
print(f'Perímetro: {ret1.perimetro()} cm, {ret2.perimetro()} cm')
ret1.AjustarCasa()

# 30X18 = 540 m²  ; piso = 10 m <<<54>>>