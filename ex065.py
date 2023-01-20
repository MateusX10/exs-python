# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
#mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
maior = menor = media = soma = cont =  0
r = ""

while True:
    cont += 1
    n = int(input("Digite um valor: "))
    
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n

    soma += n

    while True:
        r = str(input("Continuar [S/N]? ")).strip().upper()[0]
        if r in "SsNn":
            break
        print("\033[1;31mEntrada de dados inválida.Por favor, tente outra vez.\033[m")
    if r == "N":
        break

media = (soma / cont) 
print(f"O maior valor digitado foi {maior} e o menor foi {menor}")
print(f"Foram digitados ao todo {cont} números e a média entre eles vale {media}")
