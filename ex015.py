preco = 0

QuantidadeKmPercorridos = float(input("Quantos Km rodados? "))
QuantidadeDeDiasAlugado = int(input("O carro foi alugado por quantos dias? "))

preco = (QuantidadeKmPercorridos * 0.15) + (QuantidadeDeDiasAlugado * 60) 

print(f'''Tendo alugado o carro por {QuantidadeDeDiasAlugado} dias e percorrido
{QuantidadeKmPercorridos}Km, você deverá pagar ao final R${preco:.2f}''')