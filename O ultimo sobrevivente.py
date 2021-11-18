def finalcarlos():
    print("Ao chegar no outro lado do penhasco você avista a praia")
    import time
    time.sleep(3)
    print("Ao longe você avista um navío procurando sobreviventes")
    print("Parabéns você foi resgatado!")
    import time
    time.sleep(10)

def caminhoparaponte():
    print("Após passar a noite perto da fogueira,")
    import time
    time.sleep(3)
    print("Você finalmente acordou!")
    indoparaponte = input("Agora você pode ver um cânion""\n""mais abaixo há uma ponte""\n""ação >").lower()
    if "ajuda" in indoparaponte:
        comandos()
        import time
        time.sleep(3)
        caminhoparaponte()
    elif "a" in indoparaponte:
        print("Você ANDOU até o início da ponte!")
        import time
        time.sleep(4)
        print("\n""A ponte é feita de cordas,parece bastante frágil!")
        travessia = input("como você vai atravessar a ponte?""\n""ação >" ).lower()
        if "a" in travessia:
            print("Você atravessou a ponte lenta e cuidadosamente""\n""por sorte ela não se quebrou")
            import time
            time.sleep(5)            
            finalcarlos()
        elif "c" in travessia:
            print("você tentou correr em uma ponte frágil")
            import time
            time.sleep(3)
            queda = input("A ponte quebrou e você está pendurado em uma das extremidades""\n""ação >" ).lower()
            if "s" in queda:
                ("você conseguiu subir na ponte quebrada, parabéns!")
                finalcarlos()
            else:
                print("Você caiu da ponte")
                import time
                time.sleep(5)
                print("Carlos morreu na queda!")
                import time
                time.sleep(3)
                fim_de_jogo_Carlos()   
        elif "r" in travessia:
            print("Você atravessou a ponte lenta e cuidadosamente""\n""por sorte ela não se quebrou")
            import time
            time.sleep(5)            
            finalcarlos()
        else:
            print("você não pode atravessar a ponte dessa maneira!")            
    elif "p" in indoparaponte:
        print("Não tem nada para pegar aqui!")
        import time
        time.sleep(3)
        caminhoparaponte()    
    elif "s" in indoparaponte:
        print("você não tem porque subir em algum lugar agora")
        import time
        time.sleep(3)
        caminhoparaponte()
    elif "n" in indoparaponte:
        print("Você nao pode NADAR aqui!")
        import time
        time.sleep(3)
        caminhoparaponte()
    elif "r" in indoparaponte:
        print("Você vai demorar para chegar na ponte rastejando")
        import time
        time.sleep(15)
        print("Você RASTEJOU até o início da ponte!")
        import time
        time.sleep(4)
        print("\n""A ponte é feita de cordas,parece bastante frágil!")
        travessia = input("como você vai atravessar a ponte?""\n""ação >" ).lower()
        if "a" in travessia:
            print("Você atravessou a ponte lenta e cuidadosamente""\n""por sorte ela não se quebrou")
            import time
            time.sleep(5)            
            finalcarlos()
        elif "c" in travessia:
            print("você tentou correr em uma ponte frágil")
            import time
            time.sleep(3)
            queda = input("A ponte quebrou e você está pendurado em uma das extremidades""\n""ação >" ).lower()
            if "s" in queda:
                ("você conseguiu subir na ponte quebrada, parabéns!")
                finalcarlos()
            else:
                print("Você caiu da ponte")
                import time
                time.sleep(5)
                print("Carlos morreu na queda!")
                import time
                time.sleep(3)
                fim_de_jogo_Carlos()
        elif "r" in travessia:
            print("Você atravessou a ponte lenta e cuidadosamente""\n""por sorte ela não se quebrou")
            import time
            time.sleep(5)            
            finalcarlos()
        else:
            print("você não pode atravessar a ponte dessa maneira!")        
    else:
        print("você não digitou nenuma das opções válidas")
        import time
        time.sleep(3)
        caminhoparaponte()
def rotadamortecarlos():
    print("Você continuou lutando arduamente para sair da floresta")
    import time
    time.sleep(3)
    print("    Sem agua e sem abrigo, perdido em uma ilha")
    import time
    time.sleep(3)
    print("          Você foi morto por um tigre")
    fim_de_jogo_Carlos() 

def fim_de_jogo_Carlos():
    import time
    time.sleep(6)
    print("FIM DE JOGO")
    import time
    time.sleep(6)
    inicio()

def carloscomitens():
    foradoavião = input("Você precisa buscar ajuda, está escurecendo""\n""ação >").lower()
    if "ajuda" in foradoavião:
        comandos()
        import time
        time.sleep(3)
        carloscomitens()
    elif "a" in foradoavião:
        print("Você está ANDANDO na floresta e está escurecendo")
        import time
        time.sleep(4)
        print("\n""Você vê uma gruta, talvez possa fazer uma fogueira e se abrigar")
        fogueira = input("você pegou os itens dos cadáveres no avião?""\n" "s para sim n para não" )
        if "s" in fogueira:
            print("Parabéns isso foi inteligente,você usou o isqueiro para fazer""\n""uma fogueira e se abrigou durante a noite")
            import time
            time.sleep(5)            
            caminhoparaponte()
        else:
            print("você tem certeza que não pegou os itens?")
            carloscomitens()
        
    elif "c" in foradoavião:
        print("Você CORREU na floresta escura, tropeçou e caiu de um penhasco")
        import time
        time.sleep(5)
        print("Carlos morreu na queda!")
        fim_de_jogo_Carlos()        
    elif "s" in foradoavião:
        print("Você está em um vale e está escurecendo, não adianta subir nas arvores...")
        import time
        time.sleep(3)
        carloscomitens()
    elif "n" in foradoavião:
        print("Você nao pode NADAR aqui!")
        import time
        time.sleep(3)
        carloscomitens()
    elif "r" in foradoavião:
        print("Você está em uma floresta, porque rastejar quando não se é uma cobra?")
        import time
        time.sleep(3)
        carloscomitens()
    else:
        print("você não digitou nenuma das opções válidas")
        import time
        time.sleep(3)
        carloscomitens()

def carlossemitens():
    foradoavião = input("Você precisa buscar ajuda, está escurecendo""\n""ação >").lower()
    if "ajuda" in foradoavião:
        comandos()
        import time
        time.sleep(3)
        carlossemitens()
    elif "a" in foradoavião:
        print("Você está ANDANDO na floresta e está escurecendo")
        import time
        time.sleep(4)
        print("\n""Você vê uma gruta, talvez possa fazer uma fogueira e se abrigar")
        fogueira = input("você pegou os itens dos cadáveres no avião?""\n" "s para sim n para não" )
        if "s" in fogueira:
            print("Você realmente acha que eu escrevi todo esse código""\n""para se enganado?")
            carlossemitens()
        else:
            rotadamortecarlos()
        
    elif "c" in foradoavião:
        print("Você CORREU na floresta, tropeço e caiu de um penhasco")
        import time
        time.sleep(5)
        print("Carlos morreu na queda!")
        fim_de_jogo_Carlos()        
    elif "s" in foradoavião:
        print("Você está em um vale e está escurecendo, não adianta subir nas arvores...")
        import time
        time.sleep(3)
        carlossemitens()
    elif "n" in foradoavião:
        print("Você nao pode NADAR aqui!")
        import time
        time.sleep(3)
        carlossemitens()
    elif "r" in foradoavião:
        print("Você está em uma floresta, porque rastejar quando não se é uma cobra?")
        import time
        time.sleep(3)
        carlossemitens()
    else:
        print("você não digitou nenuma das opções válidas")
        import time
        time.sleep(3)
        carlossemitens()

def carlos():
    print("\n""\t""\t""\t""\t""\t""Carlos acorde!""\n"" você precisa sair desse lugar!")
    aviaocarlos = input("ação >").lower()
    if "ajuda" in aviaocarlos:
        comandos()
        import time
        time.sleep(3)
        carlos()
    elif "a" in aviaocarlos:
        itenscarlos()
    elif "c" in aviaocarlos:
        print("Você não pode CORRER, está ferido")
        import time
        time.sleep(3)
        carlos()
    elif "s" in aviaocarlos:
        print("Você está dentro de um avião não tem onde SUBIR")
        import time
        time.sleep(3)
        carlos()
    elif "n" in aviaocarlos:
        print("Você nao pode NADAR aqui!")
        import time
        time.sleep(3)
        carlos()
    elif "r" in aviaocarlos:
        print("Não tem espaço para RASTEJAR na cabine")
        import time
        time.sleep(3)
        carlos()
    else:
        print("você não digitou nenuma das opções válidas")
        import time
        time.sleep(3)
        carlos()
def itenscarlos():
    isqueiroagua = input("Você ANDOU até a cabine, o piloto e o co-piloto estão mortos""\n""O piloto tem um maço de cigarros no bolso. ""\n""O co-piloto tem uma garrafa com agua em um suporte""\n""ação >").lower()
    if "ajuda" in isqueiroagua:
        comandos()
        import time
        time.sleep(3)
        itenscarlos
    elif "a" in isqueiroagua:
        print("você saiu do avião")
        carlossemitens()
    elif "c" in isqueiroagua:
        print("Você não pode CORRER, está ferido")
        import time
        time.sleep(3)
        itenscarlos()
    elif "s" in isqueiroagua:
        print("Você está dentro de um avião não tem onde SUBIR")
        import time
        time.sleep(3)
        itenscarlos()
    elif "n" in isqueiroagua:
        print("Você nao pode NADAR aqui!")
        import time
        time.sleep(3)
        itenscarlos()
    elif "r" in isqueiroagua:
        print("Não tem espaço para RASTEJAR no avião, os corpos o impedem")
        import time
        time.sleep(3)
        itenscarlos()
    elif "p" in isqueiroagua:
        print("você pegou os itens nos cadáveres")
        import time
        time.sleep(3)
        carloscomitens()
    else:
        print("você não digitou nenuma das opções válidas")
        import time
        time.sleep(3)
        itenscarlos()
def comandos():
    print("\t""\t""\t""\t""CORRER(C)  RASTEJAR(R) SUBIR(S) ANDAR(A) NADAR(N) PEGAR(P)")
    print("\t""\t""\t""\t"" " " ""Use o comando (ajuda) para ver essa lista novamente")
    print("\t""\t""\t""\t""Quando a palavra ação aparecer,você deve digitar um comando")

def inicio():
    print("                                           O ÚLTIMO SOBREVIVENTE                          ")
    print(" Houve um acidente de avião, você sobreviveu e está em uma das três partes da fuselagem do avião que caiu, o avião")
    print("            se chocou com o cume de um vulcão em uma ilha e suas partes se dividiram em 3 locais da ilha,") 
    print("                             você estará na pele de um dos 3 sobreviventes.")
    print("\n")
    import time
    time.sleep(10)
    print("	     Carlos                              Roberto                              Luana      ")
    print("  É um homem magro de 36 anos          É um jovem forte de 25 anos       Uma moça de família, de alta classe ")
    print(" é inteligente porém sedentário      tem agilidade e um corpo atlético   tem 19 anos, é resistente, no entanto")
    print("                                       mas não é muito inteligente        não tem um estomago muito forte...")
    import time
    time.sleep(10)
    print("\n""\n""\n")
    print("                                     Você deseja seguir para um tutorial?")
    print("                                   Ou quer começar o jogo mesmo sem saber os") 
    print("                                                  comandos?                  ")
    import time
    time.sleep(5)
    print("\n")
    tutorial = input("\t""\t""Digite (s) para sim ou (n) para não,esse padrão se repetirá durante o jogo !  ")
    if "ajuda" in tutorial:
        comandos()
        import time
        time.sleep(3)    
    elif "s" in tutorial :
        print("\n""\n")
        print("\t""Para qualquer um dos personagens que você escolher, você terá a dura tarefa de sobreviver em uma ilha perdida")
        print("\t""isso significa que você terá que passar por locais perigosos, enfrentar criaturas desconhecidas, terrenos difíceis")
        print("\t""\t""e utilizar a inteligencia para sobreviver os comandos serão a primeira letra dos verbos""\n" "\t""\t""\t""\t""e você controlará seu personagem através deles")
        print( "\t""\t""\t""\t""\t""\t""são eles:")
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
            import time
            time.sleep(5)
            inicio()
inicio()