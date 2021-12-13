# 0. jogo multiplayer
# 1. uma palavra será escolhida
# 2. usuário tenta acertar uma letra
#    2.1 se acertar recebe mensagem que acertou e ele pode tentar outra letra
#    2.2 se errar recebe mensagem que errou e aparece uma parte do corpo
#    2.3 ao perder vai pro próximo jogador.
# 3. Jogo finaliza quando um dos jogadores acertar a palavra
# 4. jogo finaliza quando todos errarem e esgotarem as chances.


multiplayer = ["jogador1", "jogador2", "jogador3", "jogador4", "jogador5"]  # referente regra 0

def jogador1():
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
        print(f"Jogador atual é {multiplayer[jogador_atual]}")
        letra = input("Digite uma letra:  ")
        if letra in palavra_secreta:
            print("Você acertou. ")
            palavra_secreta = palavra_secreta.replace("_", letra)  # regra 2.1
        else:
            print("ERROU! Errou feio, errou rude!")  # regra 2.2
            print(corpo[erros])
            erros += 1
            if jogador_atual == len(multiplayer) - 1:
                jogador_atual = 0
            else:
                jogador_atual += 1

def jogador2():
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
        print(f"Jogador atual é {multiplayer[jogador_atual]}")
        letra = input("Digite uma letra:  ")
        if letra in palavra_secreta:
            print("Você acertou. ")
            palavra_secreta = palavra_secreta.replace("_", letra)  # regra 2.1
        else:
            print("ERROU! Errou feio, errou rude!")  # regra 2.2
            print(corpo[erros])
            erros += 1
            if jogador_atual == len(multiplayer) - 1:
                jogador_atual = 0
            else:
                jogador_atual += 1

def jogador3():
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
        print(f"Jogador atual é {multiplayer[jogador_atual]}")
        letra = input("Digite uma letra:  ")
        if letra in palavra_secreta:
            print("Você acertou. ")
            palavra_secreta = palavra_secreta.replace("_", letra)  # regra 2.1
        else:
            print("ERROU! Errou feio, errou rude!")  # regra 2.2
            print(corpo[erros])
            erros += 1
            if jogador_atual == len(multiplayer) - 1:
                jogador_atual = 0
            else:
                jogador_atual += 1