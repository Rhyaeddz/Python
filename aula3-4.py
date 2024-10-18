'''
Repetições
while (enquanto)
Execute uma ação enquanto condição for verdadeira
'''

condicao = True

while condicao:
    nome = input('qual  seu nome? ')
    print(f'Seu nome é {nome}.')

    if nome =='Sair':
        print('Saindo')
    break