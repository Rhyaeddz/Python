# Operadores in e not in 
# Strings são iteráveis (vc pode navegar item por item)
#   0 1 2 3 4 5
#   R a f a e l 
#  -6-5-4-3-2-1

# nome = 'Rafael'
# # print(nome[0])

# print('Ra' in nome)
# print('Rala' not in nome)

nome = input('digite seu nome: ').lower()
encontrar = input('O que deseja encontrar no nome? ').lower()

if encontrar in nome:
    print(f'{encontrar}, faz parte de {nome}.')
else:
    print(f'{encontrar}, não faz parte de {nome}.')
