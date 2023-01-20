from math import factorial
n = int(input("Digite um número para calcular o seu fatorial: "))
'''f = 1
print(f"Calculando o fatorial de {n}!")


for num in range(n, 0, -1):
    f *= num
    print(f"{num} x " if num != 1 else f"{num} = ", end='')
print(f"{f}")'''

c = n
f = 1

while c != 0:
    print(f"{c} x " if c != 1 else f"{c} = {f}", end='')
    f *= c
    c -= 1

'''print(f"O fatorial de {n} é {factorial(n)}")'''