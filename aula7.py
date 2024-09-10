# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variaveis com letras minúsculas, pode usar números e underline_.
# O sinal de = é o operador de atribuição. Ele é usado para atrubuir um valor a um nome (variavel).

# nameAndFavoriteNumber = 'Beguerjonson', 69
# print(nameAndFavoriteNumber)

nome = "rhyas"
idade = 20
maior_de_idade = idade >= 18

print("Nome:", nome)
print("Idade:", idade)
# print("É maior?", maior_de_idade)

if idade <0 or idade >120:
    print("idade invalida, voce tem", idade,)
elif maior_de_idade:
    print("Maior de idade,voce tem:", idade, "anos")
else:
    print("Menor de idade")

