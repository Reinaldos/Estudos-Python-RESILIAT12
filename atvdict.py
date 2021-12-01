glossario = {'String': 'Variável composta por letras.', 'Variável':'Valor armazenado em sistema, definido pelo usuário ou não.', 
'Lista':'Conjunto de valores', 'Algorítimo':'Sequência de passos determinada.', 'Len()':'Comando que determina o comprimento de um valor'}

def pergunta1():
    pergunta = input('Digite a palavra a ser pesquisada:')
    print(glossario.get(pergunta))
    pergunta1()
pergunta1()
