#-*-coding:utf8;-*-
numeros_pares = list()

def RetornaNumerosParesDeUmIntervalo():
  inicio = int(input('Informe o início: '))
  fim = int(input('Informe o fim: '))
  return [num for num in range(inicio, fim + 1) if num % 2 == 0]

print(f'Números pares do intervalo: {RetornaNumerosParesDeUmIntervalo()}')
