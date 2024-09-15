# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variaveis com letras minúsculas, pode usar números e underline_.
# O sinal de = é o operador de atribuição. Ele é usado para atrubuir um valor a um nome (variavel).

# nameAndFavoriteNumber = 'Beguerjonson', 69
# print(nameAndFavoriteNumber)

nome = input('qual o seu nome?')
idade = input('qual a sua idade?')

intIdade = int(idade)

maior_de_idade = (intIdade) >= 18


if intIdade <0 or intIdade >120:
    print("idade invalida, voce tem", idade,'anos ?')
elif maior_de_idade:
    print("Maior de idade,voce tem:", idade, "anos")
else:
    print("Menor de idade!")


