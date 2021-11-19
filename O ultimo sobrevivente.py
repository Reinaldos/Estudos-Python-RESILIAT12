#O CÓDIGO PODERIA ESTAR MELHOR ORGANIZADO, MAS EU NÃO TIVE TEMPO!#desculpa!
#O CÓDIGO ABAIXO SE REFERE AO PERSONAGEM ROBERTO
import time
def finalroberto():
    print("Voce subiu em uma rocha e conseguiu acenar para um Helicóptero")
    print("Parabéns você foi resgatado!")
    time.sleep(3)
    inicio()
def morteroberto():
    print("Você não pensou em suas decisões, isso fez o Roberto morrer!")
    time.sleep(3)
    inicio()

def soberoberto():
    robertorocha = input("O que você faz agora?""\n""ação >").lower()
    if "s" in robertorocha:
        print("você subiu em uma das rochas onde o avião estava apoiado!")
        time.sleep(3)
        finalroberto()
    elif "a" in robertorocha:
        print("Você andou até uma das rochas em que o avião se apoiara,ele está entre uma fenda nas rochas ")
        time.sleep(3)
        soberoberto()
    elif "c" in robertorocha:
        print("Você tentou correr, mas isso fez o avião cair")
        time.sleep(3)
        morteroberto()
    elif "r" in robertorocha:
        print("Você rastejou até uma rocha em que o avião se apoiara,ele está entre uma fenda nas rochas ")
        time.sleep(3)
        soberoberto()
    elif "p" in robertorocha:
        print("Não tem o que pegar aqui")
        time.sleep(3)
        robertofora()
    elif "n" in robertorocha:
        print("Porque você acha que pode nadar sobre um avião em chamas?")
        time.sleep(3)
        robertofora()

def robertofora():
    roberto1 = input("\n""ação >").lower()
    if "s" in roberto1:
        print("De cima do avião pegando fogo, não tem onde subir")
        time.sleep(3)
    elif "a" in roberto1:
        print("Você andou até uma das rochas em que o avião se apoiara,ele está entre uma fenda nas rochas ")
        time.sleep(3)
        soberoberto()
    elif "c" in roberto1:
        print("Você tentou correr, mas isso fez o avião cair")
        time.sleep(3)
        morteroberto()
    elif "r" in roberto1:
        print("Você rastejou até uma rocha em que o avião se apoiara,ele está entre uma fenda nas rochas ")
        time.sleep(3)
        soberoberto()
    elif "p" in roberto1:
        print("Não tem o que pegar aqui")
        time.sleep(3)
        robertofora()
    elif "n" in roberto1:
        print("Porque você acha que pode nadar sobre um avião em chamas?")
        time.sleep(3)
        robertofora

    
def roberto():
    robertoavião = input("Roberto, o avião está pegando fogo, você precisa sair daí!""\n""ação >").lower()
    if "s" in robertoavião:
        print("você subiu por uma das janelas quebradas do avião, mas ainda precisa sair de cima dele")
        time.sleep(3)
        robertofora()
    else:
        print("Tome outra decisão ou vai virar churrasco!")
#O CÓDIGO ABAIXO É REFERENTE AO PERSONAGEM LUANA
def luananada():
    print('Parabéns, você escapou do urso nadando!'"\n""\n")
    time.sleep(3)
    print('Ao chegar ao outro lado do rio você encontra outra parte da fuselagem'"\n""\n")
    time.sleep(3)
    print('Você encontra um celular em um dos corpos'"\n""\n")
    time.sleep(3)
    print('Você consegue fazer uma ligação e espera o resgate'"\n""\n")
    time.sleep(3)
    print('Parabéns você foi resgatada!'"\n""\n")
    inicio()
def nada_ou_corre():
    nadar_ou_correr = ["s","n"]
    responda = ""
    while responda not in nadar_ou_correr:
        responda = input("Quer tentar nadar ou correr dele?""\t"" N para Nadar E C para Correr""\n""ação >").lower()
        if "n" in responda :
            luananada()
        elif "c" in responda :
            print("Você não tinha folego o suficiente para fugir, o urso te matou")
        time.sleep(10)
        morteluana()
def luanaescapaurso():
    fugir_ou_esperar = ["s","n"]
    responda = ""
    while responda not in fugir_ou_esperar:
        responda = input("Quer tentar fugir ou esperar ele ir embora?""\t"" F para fugir E para esperar""\n""ação >").lower()
        if "f" in responda :
            luanafogeurso()
        elif "e" in responda :
            print("Quanto tempo você acha que um urso pode esperar por uma presa?")
        time.sleep(10)
        luanaescapaurso()
    else: 
        print("Responda uma das opções validas!.\n")
def morteluana():
    print("você não pensou nas suas decisões, por isso Luana morreu!")
    inicio()
def luanafogeurso():
    decisao = input("e agora?!""\n""ação >").lower()
    if "s" in decisao:
        print("O Urso te matou, você não tinha onde subir")
        morteluana()
    elif "ajuda" in decisao:
        comandos()
        time.sleep(3)
        luana()
    elif "P" in decisao:
        print("O Urso te matou, você não tinha o que pegar")
        time.sleep(3)
        morteluana()
    elif "a" in decisao:
        print("ANDAR não é rapido o suficiente para fugir de um urso!")
        time.sleep(3)
        morteluana()
    elif "c" in decisao:
        print("Você correu, o urso ainda está atrás de você, tem um rio na sua frente")
        time.sleep(3)
        nada_ou_corre()
    elif "n" in decisao:
        print("O urso matou uma mulher que se debatia no chão, como se estivesse nadando!!")
        time.sleep(3)
        morteluana()
    elif "r" in decisao:
        print("O urso matou uma mulher que rastejava no chão, como se fosse uma cobra")
        time.sleep(3)
        morteluana()
    else:
        print("você não digitou nenuma das opções válidas")
        time.sleep(3)
        morteluana()

def saidaluana():

    sim_ou_não = ["s","n"]
    responda = ""
    while responda not in sim_ou_não:
        responda = input("Agora que saiu de baixo dos corpos, quer sair do avião?""\t"" s para sim n para não""\n""ação >").lower()
    if responda == "s":
        print("Há um urso fora do avião,ele te viu tome uma decisão rápida!.\n")
        luanafogeurso()
    elif responda == "n":
        print("você vê um urso fora do avião, o que você quer fazer?")
        luanaescapaurso()
    else: 
        print("Responda uma das opções validas!.\n")

def luana():#(CASO O JOGADOR ESCOLHA LUANA)
    print(f"\n""\t""\t""\t""\t""\t""Luana, se você não se mexer você morrerá!""\n"" Você sente o peso dos corpos sobre seu corpo...")
    aviaoluana = input("ação >").lower()
    if "ajuda" in aviaoluana:
        comandos()
        time.sleep(3)
        luana()
    elif "P" in aviaoluana:
        print("você está em baixo de uma pilha de cadáveres, não tem nada para pegar")
        time.sleep(3)
        luana()
    elif "a" in aviaoluana:
        print("você está em baixo de uma pilha de cadáveres, não pode ANDAR")
        time.sleep(3)
        luana()
    elif "c" in aviaoluana:
        print("você está em baixo de uma pilha de cadáveres, não pode CORRER")
        time.sleep(3)
        luana()
    elif "s" in aviaoluana:
        print("você está em baixo de uma pilha de cadáveres, não pode SUBIR!")
        time.sleep(3)
        luana()
    elif "n" in aviaoluana:
        print("Você nao pode NADAR aqui!")
        time.sleep(3)
        luana()
    elif "r" in aviaoluana:
        print("Você conseguiu sair de baixo dos corpos")
        time.sleep(3)
        saidaluana()
    else:
        print("você não digitou nenuma das opções válidas")
        time.sleep(3)
        luana()
# O CÓDIGO ABAIXO SE REFERE AO PERSONAGEM CARLOS
def finalcarlos():#(CASO O JOGADOR CONSIGA CHEGAR AO FINAL)
    print("Ao chegar no outro lado do penhasco você avista a praia")
    time.sleep(3)
    print("Ao longe você avista um navío procurando sobreviventes")
    print("Parabéns você foi resgatado!")
    time.sleep(10)
    inicio()
def caminhoparaponte():#(CASO O JOGADOR CHEGUE NA PONTE)
    print("Após passar a noite perto da fogueira,")
    time.sleep(3)
    print("Você finalmente acordou!")
    indoparaponte = input(
        "Agora você pode ver um cânion""\n""mais abaixo há uma ponte""\n""ação >").lower()
    if "ajuda" in indoparaponte:
        comandos()
        time.sleep(3)
        caminhoparaponte()
    elif "a" in indoparaponte:
        print("Você ANDOU até o início da ponte!")
        time.sleep(4)
        print("\n""A ponte é feita de cordas,parece bastante frágil!")
        travessia = input(
            "como você vai atravessar a ponte?""\n""ação >").lower()
        if "a" in travessia:
            print(
                "Você atravessou a ponte lenta e cuidadosamente""\n""por sorte ela não se quebrou")
            time.sleep(5)
            finalcarlos()
        elif "c" in travessia:
            print("você tentou correr em uma ponte frágil")
            time.sleep(3)
            queda = input(
                "A ponte quebrou e você está pendurado em uma das extremidades""\n""ação >").lower()
            if "s" in queda:
                ("você conseguiu subir na ponte quebrada, parabéns!")
                finalcarlos()
            else:
                print("Você caiu da ponte")
                time.sleep(5)
                print("Carlos morreu na queda!")
                time.sleep(3)
                fim_de_jogo_Carlos()
        elif "r" in travessia:
            print(
                "Você atravessou a ponte lenta e cuidadosamente""\n""por sorte ela não se quebrou")
            time.sleep(5)
            finalcarlos()
        else:
            print("você não pode atravessar a ponte dessa maneira!")
    elif "p" in indoparaponte:
        print("Não tem nada para pegar aqui!")
        time.sleep(3)
        caminhoparaponte()
    elif "s" in indoparaponte:
        print("você não tem porque subir em algum lugar agora")
        time.sleep(3)
        caminhoparaponte()
    elif "C" in indoparaponte:
        print("Você CORREU até o início da ponte!")
        time.sleep(4)
        print("\n""A ponte é feita de cordas,parece bastante frágil!")
        travessia = input(
            "como você vai atravessar a ponte?""\n""ação >").lower()
        if "a" in travessia:
            print(
                "Você atravessou a ponte lenta e cuidadosamente""\n""por sorte ela não se quebrou")
            time.sleep(5)
            finalcarlos()
        elif "c" in travessia:
            print("você tentou correr em uma ponte frágil")
            time.sleep(3)
            queda = input(
                "A ponte quebrou e você está pendurado em uma das extremidades""\n""ação >").lower()
            if "s" in queda:
                ("você conseguiu subir na ponte quebrada, parabéns!")
                finalcarlos()
            else:
                print("Você caiu da ponte")
                time.sleep(5)
                print("Carlos morreu na queda!")
                time.sleep(3)
                fim_de_jogo_Carlos()
    elif "n" in indoparaponte:
        print("Você nao pode NADAR aqui!")
        time.sleep(3)
        caminhoparaponte()
    elif "r" in indoparaponte:
        print("Você vai demorar para chegar na ponte rastejando")
        time.sleep(15)
        print("Você RASTEJOU até o início da ponte!")
        time.sleep(4)
        print("\n""A ponte é feita de cordas,parece bastante frágil!")
        travessia = input(
            "como você vai atravessar a ponte?""\n""ação >").lower()
        if "a" in travessia:
            print(
                "Você atravessou a ponte lenta e cuidadosamente""\n""por sorte ela não se quebrou")
            time.sleep(5)
            finalcarlos()
        elif "c" in travessia:
            print("você tentou correr em uma ponte frágil")
            time.sleep(3)
            queda = input(
                "A ponte quebrou e você está pendurado em uma das extremidades""\n""ação >").lower()
            if "s" in queda:
                ("você conseguiu subir na ponte quebrada, parabéns!")
                finalcarlos()
            else:
                print("Você caiu da ponte")
                time.sleep(5)
                print("Carlos morreu na queda!")
                time.sleep(3)
                fim_de_jogo_Carlos()
        elif "r" in travessia:
            print(
                "Você atravessou a ponte lenta e cuidadosamente""\n""por sorte ela não se quebrou")
            time.sleep(5)
            finalcarlos()
        else:
            print("você não pode atravessar a ponte dessa maneira!")
    else:
        print("você não digitou nenuma das opções válidas")
        time.sleep(3)
        caminhoparaponte()
def rotadamortecarlos():#(CASO O JOGADOR MORRA)
    print("Você continuou lutando arduamente para sair da floresta")
    time.sleep(3)
    print("    Sem agua e sem abrigo, perdido em uma ilha")
    time.sleep(3)
    print("          Você foi morto por um tigre")
    fim_de_jogo_Carlos()
def fim_de_jogo_Carlos():#(MORTE POR FICAR PERDIDO)
    time.sleep(6)
    print("FIM DE JOGO")
    time.sleep(6)
    inicio()
def carloscomitens():#(CASO O JOGADOR PEGUE OS ITENS)
    foradoavião = input(
        "Você precisa buscar ajuda, está escurecendo""\n""ação >").lower()
    if "ajuda" in foradoavião:
        comandos()
        time.sleep(3)
        carloscomitens()
    elif "a" in foradoavião:
        print("Você está ANDANDO na floresta e está escurecendo")
        time.sleep(4)
        print("\n""Você vê uma gruta, talvez possa fazer uma fogueira e se abrigar")
        fogueira = input(
            "você pegou os itens dos cadáveres no avião?""\n" "s para sim n para não""ação >").lower()
        if "s" in fogueira:
            print("Parabéns isso foi inteligente,você usou o isqueiro para fazer""\n""uma fogueira e se abrigou durante a noite")
            time.sleep(5)
            caminhoparaponte()
        else:
            print("você tem certeza que não pegou os itens?")
            carloscomitens()
    elif "c" in foradoavião:
        print("Você CORREU na floresta escura, tropeçou e caiu de um penhasco")
        time.sleep(5)
        print("Carlos morreu na queda!")
        fim_de_jogo_Carlos()
    elif "s" in foradoavião:
        print("Você está em um vale e está escurecendo, não adianta subir nas arvores...")
        time.sleep(3)
        carloscomitens()
    elif "n" in foradoavião:
        print("Você nao pode NADAR aqui!")
        time.sleep(3)
        carloscomitens()
    elif "r" in foradoavião:
        print("Você está em uma floresta, porque rastejar quando não se é uma cobra?")
        time.sleep(3)
        carloscomitens()
    else:
        print("você não digitou nenuma das opções válidas")
        time.sleep(3)
        carloscomitens()
def carlossemitens():#(CASO O JOGADOR NÃO PEGUE OS ITENS!)
    foradoavião = input(
        "Você precisa buscar ajuda, está escurecendo""\n""ação >").lower()
    if "ajuda" in foradoavião:
        comandos()
        time.sleep(3)
        carlossemitens()
    elif "a" in foradoavião:
        print("Você está ANDANDO na floresta e está escurecendo")
        time.sleep(4)
        print("\n""Você vê uma gruta, talvez possa fazer uma fogueira e se abrigar")
        fogueira = input(
            "você pegou os itens dos cadáveres no avião?""\n" "s para sim n para não""\n""ação >").lower()
        if "s" in fogueira:
            print(
                "Você realmente acha que eu escrevi todo esse código""\n""para se enganado?")
            carlossemitens()
        else:
            rotadamortecarlos()
    elif "c" in foradoavião:
        print("Você CORREU na floresta, tropeçou e caiu de um penhasco")
        time.sleep(5)
        print("Carlos morreu na queda!")
        fim_de_jogo_Carlos()
    elif "s" in foradoavião:
        print("Você está em um vale e está escurecendo, não adianta subir nas arvores...")
        time.sleep(3)
        carlossemitens()
    elif "n" in foradoavião:
        print("Você nao pode NADAR aqui!")
        time.sleep(3)
        carlossemitens()
    elif "r" in foradoavião:
        print("Você está em uma floresta, porque rastejar quando não se é uma cobra?")
        time.sleep(3)
        carlossemitens()
    else:
        print("você não digitou nenuma das opções válidas")
        time.sleep(3)
        carlossemitens()
def carlos():#(NESSE CÓDIGO ESTÁ A APRESENTAÇÃO DO PERSONAGEM CARLOS)
    print("\n""\t""\t""\t""\t""\t""Carlos acorde!""\n"" você precisa sair desse lugar!")
    aviaocarlos = input("ação >").lower()
    if "ajuda" in aviaocarlos:
        comandos()
        time.sleep(3)
        carlos()
    elif "a" in aviaocarlos:
        itenscarlos()
    elif "c" in aviaocarlos:
        print("Você não pode CORRER, está ferido")
        time.sleep(3)
        carlos()
    elif "s" in aviaocarlos:
        print("Você está dentro de um avião não tem onde SUBIR")
        time.sleep(3)
        carlos()
    elif "n" in aviaocarlos:
        print("Você nao pode NADAR aqui!")
        time.sleep(3)
        carlos()
    elif "r" in aviaocarlos:
        print("Não tem espaço para RASTEJAR na cabine")
        time.sleep(3)
        carlos()
    else:
        print("você não digitou nenuma das opções válidas")
        time.sleep(3)
        carlos()
def itenscarlos():#NESSA PARTE ESTÁ O CÓDIGO PARA OS ITENS(UMA PARTE CASO PEGUE O ITEM E OUTRA CASO CONTRÁRIO) 
    isqueiroagua = input(
        "Você ANDOU até a cabine, o piloto e o co-piloto estão mortos""\n""O piloto tem um maço de cigarros no bolso. ""\n""O co-piloto tem uma garrafa com agua em um suporte""\n""ação >").lower()
    if "ajuda" in isqueiroagua:
        comandos()
        time.sleep(3)
        itenscarlos
    elif "a" in isqueiroagua:
        print("você saiu do avião")
        carlossemitens()
    elif "c" in isqueiroagua:
        print("Você não pode CORRER, está ferido")
        time.sleep(3)
        itenscarlos()
    elif "s" in isqueiroagua:
        print("Você está dentro de um avião não tem onde SUBIR")
        time.sleep(3)
        itenscarlos()
    elif "n" in isqueiroagua:
        print("Você nao pode NADAR aqui!")
        time.sleep(3)
        itenscarlos()
    elif "r" in isqueiroagua:
        print("Não tem espaço para RASTEJAR no avião, os corpos o impedem")
        time.sleep(3)
        itenscarlos()
    elif "p" in isqueiroagua:
        print("você pegou os itens nos cadáveres")
        time.sleep(3)
        carloscomitens()
    else:
        print("você não digitou nenuma das opções válidas")
        time.sleep(3)
        itenscarlos()
def comandos():
    print("\t""\t""\t""\t""CORRER(C)  RASTEJAR(R) SUBIR(S) ANDAR(A) NADAR(N) PEGAR(P)")
    print("\t""\t""\t""\t"" " " ""Use o comando (ajuda) para ver essa lista novamente")
    print("\t""\t""\t""\t""Quando a palavra ação aparecer,você deve digitar um comando")
def inicio():#ESSA PARTE CORRESPONDE A PRIMEIRA PARTE DO JOGO, É A PRINCIPAL É A FUNÇÃO INICIO
    print("                                           O ÚLTIMO SOBREVIVENTE                          ")
    print(" Houve um acidente de avião, você sobreviveu e está em uma das três partes da fuselagem do avião que caiu, o avião")
    print("            se chocou com o cume de um vulcão em uma ilha e suas partes se dividiram em 3 locais da ilha,")
    print("                             você estará na pele de um dos 3 sobreviventes.")
    print("\n")
    time.sleep(10)
    print("	     Carlos                              Roberto                              Luana      ")
    print("  É um homem magro de 36 anos          É um jovem forte de 25 anos       Uma moça de família, de alta classe ")
    print(" é inteligente porém sedentário      tem agilidade e um corpo atlético   tem 19 anos, é resistente, no entanto")
    print("                                       mas não é muito inteligente        não tem um estomago muito forte...")
    time.sleep(10)
    print("\n""\n""\n")
    print("                                     Você deseja seguir para um tutorial?")
    print("                                   Ou quer começar o jogo mesmo sem saber os")
    print("                                                  comandos?                  ")
    time.sleep(5)
    print("\n")
    tutorial = input(
        "\t""\t""Digite (s) para sim ou (n) para não,esse padrão se repetirá durante o jogo !  ")
    if "ajuda" in tutorial:
        comandos()
        time.sleep(3)
    elif "s" in tutorial:
        print("\n""\n")
        print("\t""Para qualquer um dos personagens que você escolher, você terá a dura tarefa de sobreviver em uma ilha perdida")
        print("\t""isso significa que você terá que passar por locais perigosos, enfrentar criaturas desconhecidas, terrenos difíceis")
        print("\t""\t""e utilizar a inteligencia para sobreviver os comandos serão a primeira letra dos verbos""\n" "\t""\t""\t""\t""e você controlará seu personagem através deles")
        print("\t""\t""\t""\t""\t""\t""são eles:")
        print("\n""\n")
        comandos()
        print("\n""\n")
    else:
        tutorial == 2
        print("\n")
    personagem = input("\t""\t""\t"                "Se deseja jogar com Carlos digite C"" se deseja jogar com Roberto digite R""\n""\t""\t""\t""\t""mas se gostaria de jogar com Luana digite L ""\n""ação >").lower()
    if "l" in personagem:
        luana()
    elif "r" in personagem:
        roberto()
    elif "c" in personagem:
        carlos()
    else:
        print("Como você não leu as instruções no tutorial,""\n"" Vou te dar a chance de tentar outra vez")
        time.sleep(5)
        inicio()
inicio()
