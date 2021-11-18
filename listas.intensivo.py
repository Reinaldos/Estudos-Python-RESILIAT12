motos = ['kawasaky','honda','Yamaha','Kasinsky']
#acima temos uma lista de motos pois está delimitada por colchetes[]
#caso você peça ao python para imprimir a lista você terá a listagem sem
#nenhuma formatação ex:
print(motos)
#['kawasaky', 'honda', 'Yamaha', 'Kasinsky']
#o resultado da execução do print está acima
#caso você queira a exibição de um item expecífico da lista 
#você deve invocar a variável entre parenteses e 
#colocar os colchetes + a posição do item na lista ex:
print(motos[2])
#Yamaha
#o resultado da execução do print está acima
#no caso acima a posição desssa moto é a terceira, porém
#no python o primeiro item é contado como zero, o ultimo como -1
#o penúltimo -2 e assim sucesivamente ex:
print(motos[-1])
#Yamaha
#Kasinsky
#você também pode fazer formatações na hora de exibir algum dos itens
#da lista usando para isso os comandos
#.lower .upper .title ex:
print(motos[2].upper())
#Yamaha
#Kasinsky
#YAMAHA(foi modificado com o comando .upper())
#você também pode mudar as variáveis de uma lista atribuido outros 
#valores ex:
motos[0] = 'suzuki'
print (motos[0].title())
#Kasinsky
#YAMAHA
#Suzuki(essa variável foi atribuida com outro valor)
