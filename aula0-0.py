

numeroStr = input('Digite um número: ')
numero = int(numeroStr)

def is_prime(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

if is_prime(numero):
    print("O número é primo")
else:
    print("O número não é primo")



# numeroStr = input('Digite um numero: ')
# numero = int(numeroStr)
# i = 0

# while i < numero:
#     print('Gustavo é gay')
#     i += 1 

# frase = 'GustavoÉGay'
# i = 0

# while i < len(frase) :
#     print(frase[0:len(frase) - i])
#     i = i + 1 

# frase = 'Gustavo é gay'
# tamanhoFrase = len(frase)
# frase = 'Gustavo é gay ' * 4
# i = 0

# while i <= (len(frase) - tamanhoFrase) - 1:
#     print(frase[0 + i:tamanhoFrase + i])
#     i += 1


# while True:
#     print(frase[0 + i:tamanhoFrase + i])
#     i += 1




numberStr = input('Digite quantas vezes rodar: ')
number = int(numberStr)


frase = 'Cetabu'
tamanhoFrase = len(frase)
frase = 'Cetabu' * 9

i = 0

while True:# i <= (len(frase) - tamanhoFrase) - 1:
    print(frase[0 + i:tamanhoFrase + i])
    i += 1

    if i > len(frase):
        i = 0