import random
import time
def inicio():#ESSA PARTE CORRESPONDE A PRIMEIRA PARTE DO JOGO, É A PRINCIPAL É A FUNÇÃO INICIO
    print("                                           BEM VINDO AO JOGO DA FORCA!                          ")
    print("                     NESSE JOGO VOCÊ RECEBERÁ UMA DICA E TERÁ DE ADIVINHAR UMA PALAVRA DIGITANDO AS LETRAS")
    print("                         CASO VOCÊ ACERTE AS LETRAS ELAS APARECERÃO NA PALAVRA,MAS CUIDADO!")
    print("                  SE VOCÊ ERRAR, VAI PASSAR A VEZ PARA OUTRA PESSOA, E ALGUÊM PODE MORRER ENFORCADO!")
    print("\n")
    time.sleep(10)
    jogador1 = input('DIGITE AQUI O NOME DO PRIMEIRO JOGADOR E APERTE ENTER : ')
    time.sleep(2)
    jogador2 = input('DIGITE AQUI O NOME DO SEGUNDO JOGADOR E APERTE ENTER : ')
    time.sleep(2)
    jogador3 = input('DIGITE AQUI O NOME DO TERCEIRO JOGADOR E APERTE ENTER : ')
    time.sleep(2)
    lista = [jogador1, jogador2, jogador3]

    sorteio = random.choice(lista)
    if sorteio == jogador1:
        player()
    elif sorteio == jogador2:
        player2()
    else:
        player3()


    print('Quem corre o risco de ser enforcado é! :', sorteio)


# lista = ["jogador1", "jogador2", "jogador3", "jogador4", "jogador5"]  # referente regra 0

def player():
    palavra_secreta = "casado" # regra 1  FELIPE JÁ FEZ A PARTE DA PALAVRA SECRETA

    # palavra_secreta = "casado"  # regra 1 FELIPE JÁ FEZ A PARTE DA PALAVRA SECRETA
    tentativas = 6
    jogador_atual = 0
    erros = 0

    corpo = []
    # corpo.append("+"*7 + "\n|       \n| \n| \n| \n| \n****") # sem cabeça
    corpo.append("+" * 7 + "\n|       \n|     👽\n| \n| \n| \n****")  # cabeça
    corpo.append("+" * 7 + "\n|       \n|     👽\n|     TT\n|     ||\n|\n|\n****")  # cabeça, tronco
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT\n|     ||\n|\n|\n****")  # cabeça, tronco, 1 braço,
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|\n|\n****")  # cabeça, tronco, 2 braços
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /\n|\n****")  # cabeça, tronco, 1 perna
    corpo.append(
        "+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /  \\\n|\n****")  # cabeça, tronco, 2 pernas

    for i in range(0, tentativas):
        print(f"Jogador atual é {lista[jogador_atual]}")
        letra = input("Digite uma letra:  ")
        if letra in palavra_secreta:
            print("Você acertou. ")
            palavra_secreta = palavra_secreta.replace("_", letra)  # regra 2.1
        else:
            print("ERROU! Errou feio, errou rude!")  # regra 2.2
            print(corpo[erros])
            erros += 1
            if jogador_atual == len(lista) - 1:
                jogador_atual = 0
            else:
                jogador_atual += 1

def player2():
    # palavra_secreta = "casado" # regra 1 FELIPE JÁ FEZ A PARTE DA PALAVRA SECRETA
    #
    # palavra_secreta = "casado"  # regra 1 FELIPE JÁ FEZ A PALAVRA SECRETA
    tentativas = 6
    jogador_atual = 0
    erros = 0

    corpo = []
    # corpo.append("+"*7 + "\n|       \n| \n| \n| \n| \n****") # sem cabeça
    corpo.append("+" * 7 + "\n|       \n|     👽\n| \n| \n| \n****")  # cabeça
    corpo.append("+" * 7 + "\n|       \n|     👽\n|     TT\n|     ||\n|\n|\n****")  # cabeça, tronco
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT\n|     ||\n|\n|\n****")  # cabeça, tronco, 1 braço,
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|\n|\n****")  # cabeça, tronco, 2 braços
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /\n|\n****")  # cabeça, tronco, 1 perna
    corpo.append(
        "+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /  \\\n|\n****")  # cabeça, tronco, 2 pernas

    for i in range(0, tentativas):
        print(f"Jogador atual é {lista[jogador_atual]}")
        letra = input("Digite uma letra:  ")
        if letra in palavra_secreta:
            print("Você acertou. ")
            palavra_secreta = palavra_secreta.replace("_", letra)  # regra 2.1
        else:
            print("ERROU! Errou feio, errou rude!")  # regra 2.2
            print(corpo[erros])
            erros += 1
            if jogador_atual == len(lista) - 1:
                jogador_atual = 0
            else:
                jogador_atual += 1

def player3():
    # palavra_secreta = "casado" # regra 1 FELIPE JÁ FEZ A PARTE DA PALAVRA SECRETA
    #
    # palavra_secreta = "casado"  # regra 1  FELIPE JÁ FEZ A PARTE DA PALAVRA SECRETA
    tentativas = 6
    jogador_atual = 0
    erros = 0

    corpo = []
    # corpo.append("+"*7 + "\n|       \n| \n| \n| \n| \n****") # sem cabeça
    corpo.append("+" * 7 + "\n|       \n|     👽\n| \n| \n| \n****")  # cabeça
    corpo.append("+" * 7 + "\n|       \n|     👽\n|     TT\n|     ||\n|\n|\n****")  # cabeça, tronco
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT\n|     ||\n|\n|\n****")  # cabeça, tronco, 1 braço,
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|\n|\n****")  # cabeça, tronco, 2 braços
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /\n|\n****")  # cabeça, tronco, 1 perna
    corpo.append(
        "+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /  \\\n|\n****")  # cabeça, tronco, 2 pernas

    for i in range(0, tentativas):
        print(f"Jogador atual é {lista[jogador_atual]}")
        letra = input("Digite uma letra:  ")
        if letra in palavra_secreta:
            print("Você acertou. ")
            palavra_secreta = palavra_secreta.replace("_", letra)  # regra 2.1
        else:
            print("ERROU! Errou feio, errou rude!")  # regra 2.2
            print(corpo[erros])
            erros += 1
            if jogador_atual == len(lista) - 1:
                jogador_atual = 0
            else:
                jogador_atual += 1 
inicio()