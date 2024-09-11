'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

'''

# ***********************************************************************************************


# doisxnumero = input('Escolha um número para ser multiplicado por 2: ')

# if doisxnumero.isdigit():

#     numeroFloat = float(doisxnumero)
#     print(f'O dobro de {doisxnumero} é {numeroFloat * 2}')

# else: 
#     print('isso não é um numero')

doisxnumero = input('Escolha um número para ser multiplicado por 2: ')

try:
    numeroFloat = float(doisxnumero)
    print(f'O dobro de {doisxnumero} é {numeroFloat * 2}')
except:
    print('isso não é um número')