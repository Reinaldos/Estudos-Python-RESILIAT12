from lista_animais_4 import lista_de_palavras
import random


#TENTAR FAZER UMA FUNÇÃO COM ESSAS DUAS VARIAVEIS
def pegar_palavra():
    palavra_secreta = random.choice(lista_de_palavras).upper()
    return palavra_secreta



#ESSA FUNÇÃO PERGUNTA SE O JOGADOR VAI JOGAR OU NÃO, SE SIM ELE EXECUTA A PROXIMA FUNÇÃO COM A PALAVRA JA ESCOLHIDA.
def jogar(palavra_secreta):
    while True:
        jogar = input('Deseja começar a jogar? S/N?:  ').upper()
        if jogar == 'N':
            print('Game Over')
            break
            #entra função pra chamar outro jogador
        elif jogar == 'S':
            print(f'A palavra escolhida tem {len(palavra_secreta)} letras.')
            print(' _ ' * len(palavra_secreta))
            # break
            escolha_letra(palavra_secreta)
        else:
            print('Resposta invalida!')

#AQUI A FUNÇÃO PERGUNTA A LETRA E VERIFICA DE ACORDO COM AS PALAVRAS NA lista PALAVRA_SECRETA  
def escolha_letra(palavra_secreta):
    while True:
        chute = input('Digite a Letra ou a Palavra: ')
        # letra_chutada = []
        # pelavra_chutada =[]
        # tentativas = 6

        if len(chute) == 1 and chute.isalpha():
            if chute in palavra_secreta:
                print(f'A letra{chute} esta correta!')
            else:
                print('Resposta incorreta!')
                break
                #chamar outro jogador
        elif len(chute) == len(palavra_secreta) and chute.isalpha():
            print(f'Parabes voce acertou a pelavra{chute}')
        else:
            print('Resposta incorreta!')
            break
            #chamar outro jogador






