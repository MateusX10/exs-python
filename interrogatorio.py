'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''


quantidade_de_respostas_positivas = 0
resposta = ''
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?",
             "Devia para a vítima?", "já trabalhou com a vítima?"]

situacao = {2:"Suspeita", 3:"Cúmplice",4:"Cúmplice", 5:"Assasino"}


#faz as perguntas para a pessoa que está sendo interrogada
def fazer_perguntas():
  global quantidade_de_respostas_positivas
  for pergunta in perguntas:
    print(f'\033[1m{pergunta} [sim ou não]')
    while True:
      resposta = str(input("Sua resposta: ")).lower().strip()[0]
      if resposta in "sn":
        break
    if resposta == "s":
      quantidade_de_respostas_positivas += 1

      
  
#Analisa as perguntas: se o suspeito responder sim para 2 ou mais perguntas, ela cai num for que vai analisar, de acordo com o #número de perguntas respondidas sim em relação ao número da chava do dicionário "situação", se a pessoa é suspeita, cúmplica ou #assassino
def analisa_perguntas():
  if quantidade_de_respostas_positivas >= 2:
    for k, v in situacao.items():
      if k == quantidade_de_respostas_positivas:
        print(f"\033[1;31m{v}\033[m")
  else:
    print("\033[1;32mInocente\033[m")



fazer_perguntas()
analisa_perguntas()