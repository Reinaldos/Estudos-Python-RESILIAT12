pizzas_amigo = ['calabresa','mussarella','romana']
pizzas_amigo.append('vegetariana')
pizzas_minhas = pizzas_amigo[:]
pizzas_minhas.append('chucrute')
print(f'minhas pizzas favoritas são{pizzas_minhas}')
print(f'as pizzas favoritas de meu amigo{pizzas_amigo}')
if 'c' in pizzas_minhas:
    print(pizzas_minhas[:])
