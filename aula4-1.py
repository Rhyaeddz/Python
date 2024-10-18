''' While/else '''

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
    break

else:
    print('O else foi excutado')
print('Fora do while')