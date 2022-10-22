l = [1,2,2,33,44,44, 11, 22, 13, 11, 44]

print(l)

x = set(l)

nova_l = x

for pos, v in enumerate(nova_l):
  print(f"{pos + 1} = {v}")