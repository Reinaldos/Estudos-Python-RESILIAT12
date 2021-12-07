glossario = {'String': 'Variável composta por letras.', 'Variável':'Valor armazenado em sistema, definido pelo usuário ou não.', 
'Lista':'Conjunto de valores', 'Algorítimo':'Sequência de passos determinada.', 'Len()':'Comando que determina o comprimento de um valor'}

glossario.update({"String":"caracteres"})
glossario["Variável"]= "feijão"
print(glossario)
del glossario ['Algorítimo']
glossario.pop('Len()')
glossario.popitem()
print(glossario)
glossario.clear()
print(glossario)
# def pergunta1():
#     pergunta = input('Digite a palavra a ser pesquisada:')
#     print(glossario.get(pergunta))
#     pergunta1()
# pergunta1()
