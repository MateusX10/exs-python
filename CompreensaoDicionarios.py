var = {i: i ** 2 for i in range(0,10)}
for i, v in var.items():
  print(f'Indíce: {i} valor: {v}')

palavra = 'dragão'

indice_palavra = {palavra.index(i): i for i in palavra}
print(indice_palavra)