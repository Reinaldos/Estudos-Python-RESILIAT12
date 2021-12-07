def localizacao(cidade, país='Brasil'): #PARAMENTROS DEFAULT, MESMO SEM ARGUMENTO ELE COMPLETA
    print(f'A cidade é {cidade}, localizada em {país}')

localizacao(cidade='Rio de Janeiro')
localizacao(cidade='Foz do Iguaçu')
localizacao(cidade='Nova York', país='EUA')