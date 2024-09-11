"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str.

"""

variavel = 'Olá mundo'
print(variavel[4:])

nome = input('Qual seu nome? ')
QntLetrasNome = input(f'seu nome tem {len(nome)} letras? ')

if QntLetrasNome == 'sim':
    print('certo')
else:
    print('Você por acaso é burro?')
