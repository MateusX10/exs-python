print("-=" * 40)
print("\033[1;34m10 TERMOS DE UMA PA \033[m".center(80))
print("-=" * 40)

PrimeiroTermo = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
fim = PrimeiroTermo + razao * 10
for v in range(PrimeiroTermo, fim, razao):
    print(f"{v} --> ", end='')
print("FIM")