from typing import Final
from lista_animais_4 import lista_de_palavras
import random
import time
def final():
   print ('não foi dessa vez!')
   restart = input ('você gostaria de jogar novamente? ''\n').lower()
   if 's' in restart:
       inicio()
   else:
       print('FIM DE JOGO')

    
def inicio():#FUNÇÃO PARA TITULO DO JOGO E ESCOLHA DOS JOGADORES
    print("                                           BEM VINDO AO JOGO DA FORCA!                          ")
    print("                     NESSE JOGO VOCÊ RECEBERÁ PALAVRA SECRETA E TERÁ DE ADIVINHAR  DIGITANDO AS LETRAS")
    print("                         CASO VOCÊ ACERTE AS LETRAS ELAS APARECERÃO NA PALAVRA,MAS CUIDADO!")
    print("                  SE VOCÊ ERRAR, VAI PASSAR A VEZ PARA OUTRA PESSOA, E ALGUÊM PODE MORRER ENFORCADO!")
    print("\n")
    # time.sleep(5)
    jogador1 = input('DIGITE AQUI O NOME DO PRIMEIRO JOGADOR E APERTE ENTER : ')
    # time.sleep(1)
    jogador2 = input('DIGITE AQUI O NOME DO SEGUNDO JOGADOR E APERTE ENTER : ')
    # time.sleep(1)
    jogador3 = input('DIGITE AQUI O NOME DO TERCEIRO JOGADOR E APERTE ENTER : ')
    # time.sleep(1)
    lista = [jogador1, jogador2, jogador3]
    palavra_secreta = random.choice(lista_de_palavras).upper()
    print(f'a palavra tem  {len(palavra_secreta)}  '"letras")
    print('_ _'*len(palavra_secreta))
    multiplayer = lista  # referente regra 0
    

    # def jogador1():
    # regra 1  FELIPE JÁ FEZ A PARTE DA PALAVRA SECRETA

    # palavra_secreta = "casado"  # regra 1 FELIPE JÁ FEZ A PARTE DA PALAVRA SECRETA

    tentativas = 18
    jogador_atual = 0
    erros = 0
    erros2 = 0
    erros3 = 0

    corpo = []
    # corpo.append("+"*7 + "\n|       \n| \n| \n| \n| \n") # sem cabeça
    corpo.append("+" * 7 + "\n|       \n|     👽\n| \n| \n| \n")  # cabeça
    corpo.append("+" * 7 + "\n|       \n|     👽\n|     TT\n|     \n|\n|\n**")  # cabeça, tronco
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT\n|     \n|\n|\n")  # cabeça, tronco, 1 braço,
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|\n|\n")  # cabeça, tronco, 2 braços
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     \n|    /\n|\n**")  # cabeça, tronco, 1 perna
    corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     \n|    /  \\n|\n**")  # cabeça, tronco, 2 pernas

    corpo2 = []
    # corpo.append("+"*7 + "\n|       \n| \n| \n| \n| \n") # sem cabeça
    corpo2.append("+" * 7 + "\n|       \n|     👽\n| \n| \n| \n")  # cabeça
    corpo2.append("+" * 7 + "\n|       \n|     👽\n|     TT\n|     \n|\n|\n**")  # cabeça, tronco
    corpo2.append("+" * 7 + "\n|       \n|     👽\n|  o==TT\n|     \n|\n|\n")  # cabeça, tronco, 1 braço,
    corpo2.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|\n|\n")  # cabeça, tronco, 2 braços
    corpo2.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     \n|    /\n|\n**")  # cabeça, tronco, 1 perna
    corpo2.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     \n|    /  \\n|\n**")  # cabeça, tronco, 2 pernas

    corpo3 = []
    # corpo.append("+"*7 + "\n|       \n| \n| \n| \n| \n") # sem cabeça
    corpo3.append("+" * 7 + "\n|       \n|     👽\n| \n| \n| \n")  # cabeça
    corpo3.append("+" * 7 + "\n|       \n|     👽\n|     TT\n|     \n|\n|\n**")  # cabeça, tronco
    corpo3.append("+" * 7 + "\n|       \n|     👽\n|  o==TT\n|     \n|\n|\n")  # cabeça, tronco, 1 braço,
    corpo3.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|\n|\n")  # cabeça, tronco, 2 braços
    corpo3.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     \n|    /\n|\n**")  # cabeça, tronco, 1 perna
    corpo3.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     \n|    /  \\n|\n**")  # cabeça, tronco, 2 pernas
    
    # test = [corpo, corpo2, corpo3]
   
    for i in range(0, tentativas):
        
        print(f"Jogador atual é {multiplayer[jogador_atual]}")
        letra = input("Digite uma letra:  ")
        if letra == palavra_secreta:
            print(f"JOGADOR {multiplayer[jogador_atual]} VENCEU!!!")
            break
        elif letra in palavra_secreta:
            print("Você acertou. ")
            palavra_secreta = palavra_secreta.replace("", letra)  # regra 2.1

        elif jogador_atual == 0:
            print("ERROU! Errou feio, errou rude!")  # regra 2.2
            print(corpo[erros])
            erros += 1
            if jogador_atual == len(multiplayer) - 1:
                jogador_atual = 0
            else:
                jogador_atual += 1

        elif jogador_atual == 1:
            print("ERROU! Errou feio, errou rude!")  # regra 2.2
            print(corpo2[erros2])
            erros2 += 1
            if jogador_atual == len(multiplayer) - 1:
                jogador_atual = 0
            else:
                jogador_atual += 1

        elif jogador_atual == 2:
            print("ERROU! Errou feio, errou rude!")  # regra 2.2
            print(corpo3[erros3])
            erros3 += 1
            if jogador_atual == len(multiplayer) - 1:
                jogador_atual = 0
            else:
                jogador_atual += 1
    else:
        final()
inicio() 