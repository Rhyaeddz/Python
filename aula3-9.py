'''
Iteranddo strings com while

'''
#       012345
nome = input('Escreva seu nome: ') # Iteráveis
tamanhoNome = len(nome)

indice = 0
novoNome = ''
while indice < len(nome):
    letra = (nome[indice])
    novoNome += f'*{letra}'
    indice += 1

novoNome += '*'
print(novoNome)
