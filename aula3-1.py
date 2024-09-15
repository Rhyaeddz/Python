'''
Flag (bandeira) - Marcar um local 
none = não valor 
is e is not = é ou não é (tipo, valor , identidade)
id = identidade
'''

# v1 = 'a'
# v2 = 'ab'

# print(id(v1))
# print(id(v2))

condição = False
passouNoIf = None

if condição:
    passouNoIf = True
    print('faça algo')
else:
    print('não faça algo')

if passouNoIf is None:
    print('não passou no if')
else:
    print("Passou no if")