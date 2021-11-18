#exercício faça você mesmo do livro curso intensivo de python
#nro 3.1
nomes = ['Leandro','vagner','leonardo','rafael']
print(nomes[1])
print(nomes[-1])
print(nomes[2].lower())
print(nomes[3].upper())
print(nomes[-3].title())
#exercício faça você mesmo do livro curso intensivo de python
#nro 3.2
print('esse é meu melhor amigo '+ nomes [2].title()+' gosto muito!') 
print(nomes[3].title()+' costuma jogar muito')
print(nomes[2].upper()+' esse é uma figura')
print('mas '.title()+ 'nenhum deles se compara a '+nomes[0] )
#exercício faça você mesmo do livro curso intensivo de python
#nro 3.3
motos = ['honda','suzuki','ducati','bmw']
print('eu gostaria de ter uma '.title()+motos[0].upper()+' pra tirar uma chinfra'.upper())
motos[0] = 'ferrari'
print('eu gostaria de ter uma '.title()+motos[0].upper()+' pra tirar uma chinfra'.upper())
motos.append('caloi')
print(motos)
motos.insert(2,'triumph'.upper())
print(motos)
del(motos[2])
print(motos)