'''
Interpolação básica de strings
s - string
d e i - int
f - float 
x e X - Hexadecimal (ABCDEF0123456789)
'''
nome = 'Rhyas'
moeda = 'doláres'
preco = 100.696969
variavel = '%s, o preço é $%.2f %s' % (nome, preco,moeda)
print(variavel)
print('O hexadecimal de %d é %04X' % (1500,1500))
