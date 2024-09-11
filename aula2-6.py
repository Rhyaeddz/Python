# Formatação básica de strings
# s - string 
# d - int 
# f - float 
# .<número de dígitos>f
# x ou X - Hexadecimal
# (caractere)(><^)(quantidade)
# > - esquerda
# < - direita
# ^ - centro
# Sinal - + ou -
# Ex.: 0>100,.1f
# Conversion flags - !r !s !a


variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >20}')
print(f'{variavel: <20}')
print(f'{variavel: ^20}')
print(f'{12.3456789:.2f}')
print(f'O hexadecimal de 1500 é {1500:04x}')