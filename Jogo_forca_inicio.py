
from codigo_amanda import jogador1
from lista_animais_4 import lista_de_palavras
import random
import time
def inicio():#ESSA PARTE CORRESPONDE A PRIMEIRA PARTE DO JOGO, É A PRINCIPAL É A FUNÇÃO INICIO
    print("                                           BEM VINDO AO JOGO DA FORCA!                          ")
    print("                     NESSE JOGO VOCÊ RECEBERÁ UMA DICA E TERÁ DE ADIVINHAR UMA PALAVRA DIGITANDO AS LETRAS")
    print("                         CASO VOCÊ ACERTE AS LETRAS ELAS APARECERÃO NA PALAVRA,MAS CUIDADO!")
    print("                  SE VOCÊ ERRAR, VAI PASSAR A VEZ PARA OUTRA PESSOA, E ALGUÊM PODE MORRER ENFORCADO!")
    print("\n")
    # time.sleep(10)
    player1 = input('DIGITE AQUI O NOME DO PRIMEIRO JOGADOR E APERTE ENTER : ')
    # time.sleep(2)
    player2 = input('DIGITE AQUI O NOME DO SEGUNDO JOGADOR E APERTE ENTER : ')
    # time.sleep(2)
    player3 = input('DIGITE AQUI O NOME DO TERCEIRO JOGADOR E APERTE ENTER : ')
    # time.sleep(2)
    lista = [player1, player2, player3]
    
    sorteio = random.choice(lista)

    print('Quem corre o risco de ser enforcado é! :', sorteio)

    jogo(pegar_palavra())

#TENTAR FAZER UMA FUNÇÃO COM ESSAS DUAS VARIAVEIS
def pegar_palavra():
    palavra_secreta = random.choice(lista_de_palavras).upper()
    print(palavra_secreta)
    return palavra_secreta



#ESSA FUNÇÃO PERGUNTA SE O JOGADOR VAI JOGAR OU NÃO, SE SIM ELE EXECUTA A PROXIMA FUNÇÃO COM A PALAVRA JA ESCOLHIDA.
def jogo(palavra_secreta):
        jogar = input('Deseja começar a jogar? S/N?:  ').upper()
        if jogar == 'N':
            print('Game Over')
            
            #entra função pra chamar outro jogador
        elif jogar == 'S':
            print(f'A palavra escolhida tem {len(palavra_secreta)} letras.')
            print(' _ ' * len(palavra_secreta))
           
            escolha_letra(palavra_secreta)
        elif jogar != 'S' or 'N':
            print('Resposta invalida!')
        else:
            jogo(palavra_secreta)

def corpo():
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
        print(f"Jogador atual é {jogador1[jogador_atual]}")
        letra = input("Digite uma letra:  ")
        if letra in palavra_secreta:
            print("Você acertou. ")
            palavra_secreta = palavra_secreta.replace("_", letra)  # regra 2.1
        else:
            print("ERROU! Errou feio, errou rude!")  # regra 2.2
            print(corpo[erros])
            erros += 1
            if jogador_atual == len(jogador1) - 1:
                jogador_atual = 0
            else:
                jogador_atual += 1 

            
#AQUI A FUNÇÃO PERGUNTA A LETRA E VERIFICA DE ACORDO COM AS PALAVRAS NA lista PALAVRA_SECRETA  
def escolha_letra(palavra_secreta):
    chute = input('Digite a Letra ou a Palavra: ')
        # letra_chutada = []
        # pelavra_chutada =[]
        # tentativas = 6

    if len(chute) == 1 and chute.isalpha():
        if chute in palavra_secreta:
            print(f'A letra{chute} esta correta!')
        else:
            print('Resposta incorreta!')
            
                #chamar outro jogador
    elif len(chute) == len(palavra_secreta) and chute.isalpha():
        print(f'Parabes voce acertou a pelavra{chute}')
    else:
        print('Resposta incorreta!')
    escolha_letra(palavra_secreta)
            #chamar outro jogador      
inicio()
# def corpo():
#     tentativas = 6
#     jogador_atual = 0
#     erros = 0
#     corpo = []
#     # corpo.append("+"*7 + "\n|       \n| \n| \n| \n| \n****") # sem cabeça
#     corpo.append("+" * 7 + "\n|       \n|     👽\n| \n| \n| \n****")  # cabeça
#     corpo.append("+" * 7 + "\n|       \n|     👽\n|     TT\n|     ||\n|\n|\n****")  # cabeça, tronco
#     corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT\n|     ||\n|\n|\n****")  # cabeça, tronco, 1 braço,
#     corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|\n|\n****")  # cabeça, tronco, 2 braços
#     corpo.append("+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /\n|\n****")  # cabeça, tronco, 1 perna
#     corpo.append(
#         "+" * 7 + "\n|       \n|     👽\n|  o==TT==o\n|     ||\n|    /  \\\n|\n****")  # cabeça, tronco, 2 pernas

#     for i in range(0, tentativas):
#         print(f"Jogador atual é {jogador1[jogador_atual]}")
#         letra = input("Digite uma letra:  ")
#         if letra in palavra_secreta:
#             print("Você acertou. ")
#             palavra_secreta = palavra_secreta.replace("_", letra)  # regra 2.1
#         else:
#             print("ERROU! Errou feio, errou rude!")  # regra 2.2
#             print(corpo[erros])
#             erros += 1
#             if jogador_atual == len(jogador1) - 1:
#                 jogador_atual = 0
#             else:
#                 jogador_atual += 1 

