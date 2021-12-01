pilha = []

def criar_pilha(inicio, fim):
    for i in range(inicio, fim):
        acrescenta_pilha(pilha, i)

def acrescenta_pilha (pilha, elemento):
    return pilha.append(elemento)

#def remove_pilha (pilha):
#    return pilha.pop(-1)

def verifica_quantidade(pilha):
    print("A quantida de elementos é:", len(pilha))

def verifica_vazia(pilha):
    if pilha == []:
        return "pilha vazia"
    else:
        return "pilha cheia"


criar_pilha(0, 0)
print(pilha)
verifica_quantidade(pilha)
print(verifica_vazia(pilha))
