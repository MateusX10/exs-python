def RemoveVogais():
  frase = str(input('Informe uma frase para remover suas vogais: '))
  return [letra for letra in frase if letra not in ['a','e','i','o','u']]

frase_sem_vogais = ''.join(RemoveVogais())

print(f'Frase sem vogais: "{frase_sem_vogais}"')
