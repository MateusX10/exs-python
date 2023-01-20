cidade = str(input("Nome da cidade: ")).strip().upper()

if cidade.split()[0] == "SANTO":
    print(f"\033[1;32mA cidade {cidade} começa com o nome 'SANTO' \033[m")

else:
    print(f"\033[1;31mA cidade {cidade} não começa com o nome 'SANTO'\033[m")