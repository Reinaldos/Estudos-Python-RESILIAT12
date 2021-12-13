import random
import time
def inicio():#FUNÇÃO PARA TITULO DO JOGO E ESCOLHA DOS JOGADORES
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
    return lista
    
inicio()