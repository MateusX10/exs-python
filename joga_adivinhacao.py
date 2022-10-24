from random import choice
from time import sleep


def CongelarTela(tempo=1):
  sleep(tempo)

def LinhaSeparacao():
  print('\033[1;35m-=' * 30)


tentativas = QuantidadeDeDicas = 0 
PerguntaAoUsuarioSeEleQuerDica = LetraSorteadaDaDica = ""
PrimeiraTentativa = True
lista_palavras = ["gato", "cachorro", "tigre", "golfinho", "macaco", "dinossauro",
                  "girafa", "elefante", "coelho", "peixe", "aranha", "formiga" ]
#define/sorteira a palavra do jogo
palavra = choice(lista_palavras) 
LetrasDaPalavra = [letra for letra in palavra]
letras_acertadas = list()

#mensagem de boas-vindas/apresentação do jogo ao usuário
print("\033[1;34mBem-vindo ao jogo da adivinhação!")
CongelarTela()
print("Você precisará acertar qual o animal/inseto!\033[m")
CongelarTela()
print("Esta é a palavra: ")
print('\033[1m-\n' * len(palavra))
CongelarTela(2)


#início da partida
while True:
  palpite_usuario = str(input('\033[1;33mSeu palpite: \033[m'))
  tentativas += 1
  for letra in palavra:

# se o usuário acertar uma letra da palavra ou o usuário tiver digitado uma letra que ele já acertou, 
# esse bloco de código é executado.As letras acertadas pelo jogador ficam guardadas na lista 
# "letras acertadas" e logo em seguida a palavra acertada pelo jogador é removida da lista 
# "LetrasDaPalavra" (quando a lista "LetarasDaPalavra" ficar vazia, o loop do laço será interrompido 
# e a partida será encerrada).
    if palpite_usuario == letra or letra in letras_acertadas: 
      print(f'\033[1m{letra}')
      letras_acertadas.append(letra)
      if letra in LetrasDaPalavra:
        LetrasDaPalavra.remove(letra)
    
    # Imprime um "-" representando a letra que o jogador ainda não descobriu/acertou
    else:
      print('\033[1m-')

   
  #pergunta se o usuário quer dica
  if tentativas == 8 or tentativas == 14 or tentativas == 20 or tentativas >= 26:
    while True:
      PerguntaAoUsuarioSeEleQuerDica = str(input("\033[1;33mQuer uma dica [S/N]? ")).strip().upper()[0]
      if PerguntaAoUsuarioSeEleQuerDica in "SN":
        break
      print('\033[1;31mDigite somente "S" ou "N"')
    if PerguntaAoUsuarioSeEleQuerDica == "S":
      QuantidadeDeDicas += 1
      LetraSorteadaDaDica = choice(LetrasDaPalavra)
      LetrasDaPalavra.remove(LetraSorteadaDaDica)
      letras_acertadas.append(LetraSorteadaDaDica)


  #encerra o loop do laço quando o jogador acerta a palavra
  if len(LetrasDaPalavra) == 0:
    break
  LinhaSeparacao()
    

# jogador recebe essa mensagem quando vencer/encerrar o jogo
LinhaSeparacao()
print(f"\033[1;32mMuito bem!Você acertou!A palavra era \033[1;34m{palavra}\033[m") 
print(f'\033[1;33mTentativas: \033[m{tentativas} \n\033[1;33mDicas: \033[m{QuantidadeDeDicas}')   
LinhaSeparacao()