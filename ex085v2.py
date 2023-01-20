lista_numeros = list()
lista_pares = list()
lista_impares = list()

for num in range(0,7):
    n = int(input(f"Digite o {num+1}º valor: "))
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)

lista_numeros.append(lista_pares[:])
lista_numeros.append(lista_impares[:])

print("-=" * 60)
print(f"Lista completa: {lista_numeros}")

print(f"Lista dos números pares: {lista_numeros[0]}")    
print(f"Lista números ímpares: {lista_numeros[1]}")