matriz = [[0,0,0], [0,0,0], [0,0,0]]
SomaPar = SomaTerceiraColuna =  MaiorValorSegundaLinha = SomaDiagonal = 0
MaiorValorNaMatriz = MenorValorNaMatriz = 0
PosicaoMaiorValorNaMatriz = list()
PosicaoMenorValorNaMatriz = list()
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"Digite um valor para a posição [{i},{j}] da matriz: "))


print("-=" * 40)
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            SomaPar += matriz[i][j]

        if j == 2:
            SomaTerceiraColuna += matriz[i][j]

        if i == 1:
            if matriz[i][j] > MaiorValorSegundaLinha:
                MaiorValorSegundaLinha = matriz[i][j]

        if i == j:
            SomaDiagonal += matriz[i][j]

        if matriz[i][j] > MaiorValorNaMatriz:
            MaiorValorNaMatriz = matriz[i][j]
            PosicaoMaiorValorNaMatriz = [i, j]
        if i == 0 and j == 0:
            MenorValorNaMatriz = matriz[i][j]
            PosicaoMenorValorNaMatriz = [i,j]
        else:
            if matriz[i][j] < MenorValorNaMatriz:
                MenorValorNaMatriz = matriz[i][j]
                PosicaoMenorValorNaMatriz = [i,j]
        

    print()
print("-=" * 40)
print(f"A soma de todos os números pares da matriz é {SomaPar}")
print(f"A soma de todos os valores da 3º coluna é {SomaTerceiraColuna}")
print(f"O maior valor da segunda linha é {MaiorValorSegundaLinha}")
print(f"A soma das diagonais é {SomaDiagonal}")
print(f"Maior valor na matriz: {MaiorValorNaMatriz}.Posição: {PosicaoMaiorValorNaMatriz}")
print(f"Menor valor na matriz: {MenorValorNaMatriz}.Posição: {PosicaoMenorValorNaMatriz}")