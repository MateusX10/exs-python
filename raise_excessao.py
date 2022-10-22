

try:
  n1 = int(input('Digite um valor: '))
  n2 = int(input('Digite outro valor: '))


except:
  raise Exception('Uma excessão ocorreu')
  
else:
    print('Curiosamente, funcionou')

finally:
    print("Volte quando puder!")

