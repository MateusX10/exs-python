matriz = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"Digite um valor para a posição [{i},{j}] da matriz: "))

print("-=" * 40)

for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]:^5}] ", end='')
    print()
    