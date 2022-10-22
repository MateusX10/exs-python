x = set()

x.add(1)
x.add(10)
x.add(10)
x.add(1)

print(x)

lista_repetida = [1,2,31,2,3,1,1,1,2,2,3,3,3,5,10,88,99,11,1,25,8,9,6,7,8,5]

print(lista_repetida)

unico = set(lista_repetida)
print('/n/n****')
print(unico)


print('-=' * 30)

y = {1,1,2,2,3,4,5}
print(y)

for v in y:
  print(v)
  
y.add((1,2,3))
print(y)
  