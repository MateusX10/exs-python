nome = str(input("Nome completo: ")).title().strip()

sem_espaco = nome.split()
primeiro_nome = sem_espaco[0]
sem_espaco = "".join(sem_espaco)

print(f'''Seu nome equivale a:
{nome.upper()} em letras maiúsculas
{nome.lower()} em letras minúsculas
Seu nome tem {len(sem_espaco)} letras
O seu primeiro nome é {primeiro_nome}''')
