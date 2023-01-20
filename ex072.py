numeros = ("zero", "um", "dois", "três", 'quatro', "cinco",
           "seis", 'sete', "oito", "nove","dez", "onze",
           "doze", "treze", "catorze", "quinze", "dezesseis",
           "dezessete", "dezoito", "dezenove", "vinte")
n = 0

while True:
    n = int(input("Digite um número entre 0 e 20: "))
    if 0 <= n <= 20:
        break
    print("\033[1;31mErro.Por favor, digite um número entre 0 e 20\033[m")

print(f"Você digitou o número {numeros[n]}")
