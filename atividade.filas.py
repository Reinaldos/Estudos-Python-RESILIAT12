def acrescenta_pilha (pilha, elemento):
    return pilha.append(elemento)

def verifica_quantidade (pilha):
    print("A quantida de elementos é:", len(pilha-1))

def verifica_vazia(pilha):
    if pilha == []:
        return "Pilha vazia"
    else:
        return "Pilha cheia"

pilha = []

for i in range(0, 20):
    acrescenta_pilha(pilha, i)

print(pilha)
verifica_quantidade(pilha)
print(verifica_vazia(pilha))
