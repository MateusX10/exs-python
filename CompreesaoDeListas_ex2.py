def RetornaVogais():
  frase = str(input('Informe uma frase: '))
  return [vogal for vogal in frase if vogal in ['a','e','i','o','u']]

print(f'O resultado é {RetornaVogais()}')