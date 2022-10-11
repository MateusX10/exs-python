#computador, pegue a borracha que derrubei, por favor!

palavras = ["computador", "PC", "máquina", "pegue", "pegar", "borracha", "chao", 
            "derrubei", "derrubar", "derrubou", "por favor", "faz favor", "favor"]

print("""Peça ao computador pegar a borracha do chão!
- Sua ordem deve incluir somente as seguintes palavras:""")
for word in palavras:
  print(f'{word} - ',end='')
while True:
  tot_palavras_corretas = 0
  ordem = str(input("\nSua ordem: ")).lower().strip().split()
  for palavra in range(0, len(ordem)):
    if ordem[palavra] in palavras:
      tot_palavras_corretas += 1
  if tot_palavras_corretas == len(ordem):
    break
  print("\033[1;31mInforme uma palavra válida!\033[m")
"".join(ordem)
print(ordem)
if "borracha" in ordem and "chao" in ordem and "pegue" in ordem:
  print('Pegando borracha...')
if "borracha" not in ordem and "pegue" and ordem  and "chao" not in ordem:
  print("Computador não entendeu o que você quis dizer")
elif "borracha" not in ordem:
  print("Computador não sabe o que precisa pegar")
elif "pegar" not in ordem or "pegue" not in ordem:
  print("Computador não entendeu o que fazer")
elif "chao" not in ordem:
  print("Computador não sabe o que é chão")
