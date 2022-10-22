try:
  for i in ['a','b','c']:
    print(i ** 2)
except:
  raise Exception('Ocorreu um erro')
else:
  print('APP bugou???')

finally:

  print('Acabamos mais um capítulo, interessante?')
