def leiaString(string):
    '''--> Recebe uma string e a valida
        Atributos:
            string(str): string a ser validade
            return: retorna a string validada
    '''

    from sys import exit


    while True:
        try:
            text = str(input(string))

        except (KeyboardInterrupt):

            exit(1) #indica ao S.O que houve um erro na execução do programa

        else:

            if text.strip() == "":
                print("\033[1;31mPor favor, informe uma string válida!\033[m")
                continue

            return text


            
def contaVogais(string)-> int:
    '''--> Retorna o número de vogais de uma string
        Parâmetros:
            string(str): string a ser analisada
            return: retorna o número de vogais da string
            
    '''

    vogais = ["a", "e", "i", "o", "u",
              "A", "E", "I", "O", "U",
              "á", "é", "í", "ó", "ú",
              "Á", "É","Í", "Ó", "Ú",
              "à", "è", "ì", "ò", "ù",
              "À", "È", "Ì", "Ò", "Ù",
              "â", "ê", "î", "ô", "û",
              "Â", "Ê", "Î", "Ô", "Û",
              "ã", "õ",
              "Ã", "Õ"]

    totalVogaisNaString = 0
    
    for letra in string:
        if letra in vogais:
            totalVogaisNaString += 1
    
    return totalVogaisNaString
