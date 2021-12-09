import time
def inicio():#ESSA PARTE CORRESPONDE A PRIMEIRA PARTE DO JOGO, É A PRINCIPAL É A FUNÇÃO INICIO
    print("                                           BEM VINDO AO JOGO DA FORCA!                          ")
    print("                     NESSE JOGO VOCÊ RECEBERÁ UMA DICA E TERÁ DE ADIVINHAR UMA PALAVRA DIGITANDO AS LETRAS")
    print("                         CASO VOCÊ ACERTE AS LETRAS ELAS APARECERÃO NA PALAVRA,MAS CUIDADO!")
    print("                  SE VOCÊ ERRAR, VAI PASSAR A VEZ PARA OUTRA PESSOA, E ALGUÊM PODE MORRER ENFORCADO!")
    print("\n")
    time.sleep(10)
def jogadores():#NESSA FUNÇÃO OS JOGADORES COLOCARÃO SEUS NOMES
    jogador1 = input('DIGITE AQUI O NOME DO PRIMEIRO JOGADOR E APERTE ENTER : ')
    time.sleep(2)
    jogador2 = input('DIGITE AQUI O NOME DO SEGUNDO JOGADOR E APERTE ENTER : ')
    time.sleep(2)
    jogador3 = input('DIGITE AQUI O NOME DO TERCEIRO JOGADOR E APERTE ENTER : ')
    time.sleep(2)
    if 'a''b''c''d''e' in jogador1:
        print (f'o jogador que começa é {jogador1}')
    elif 'i''l''f''g''h' in jogador2:
        print (f'o jogador que coméça é{jogador2}')
    else:
        print (f'o jogador que começa é {jogador3}')
inicio()
jogadores()


