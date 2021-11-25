def acrescenta_fila (fila, elemento):
    return fila.append(elemento)

def verifica_quantidade (fila):
    print("A quantida de elementos é:", len(fila))

def verifica_vazia(fila):
    if fila == []:
        return "Fila vazia"
    else:
        return "Fila cheia"

fila = []

for i in range(0, 20):
    acrescenta_fila(fila, i)

print(fila)
verifica_quantidade(fila)
print(verifica_vazia(fila))
