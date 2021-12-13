
from lista_animais_4 import lista_de_palavras
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

    print('Quem corre o risco de ser enforcado é! :', sorteio)

    jogar(pegar_palavra())

#TENTAR FAZER UMA FUNÇÃO COM ESSAS DUAS VARIAVEIS
def pegar_palavra():
    palavra_secreta = random.choice(lista_de_palavras).upper()
    return palavra_secreta



#ESSA FUNÇÃO PERGUNTA SE O JOGADOR VAI JOGAR OU NÃO, SE SIM ELE EXECUTA A PROXIMA FUNÇÃO COM A PALAVRA JA ESCOLHIDA.
def jogar(palavra_secreta):
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
            pegar_palavra()

            
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
 
        
