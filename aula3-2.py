'''
Faça um programa que peça ao usuario para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um numero inteiro.
'''

NumeroDigitado = input('Digite um número inteiro: ')

try:  

    IntNumeroDigitado = int(NumeroDigitado)
    numeroPar = IntNumeroDigitado % 2 == 0
    numeroimpar =  IntNumeroDigitado % 2 == 1  

    if numeroPar:
        print(f'O número {IntNumeroDigitado} é par. ')

    elif numeroimpar:
        print(f'O número {IntNumeroDigitado} é impar. ')

except:
    print('Isso não é um número inteiro!')   


'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horario descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa Tarde 12-17 e Boa noite 18-23.
'''

horarioAtual = input('Que horas são agora? ')

try:

    horarioAtualInt = int(horarioAtual)

    manhã = horarioAtualInt >= 6 and horarioAtualInt <= 11
    tarde = horarioAtualInt >=12 and horarioAtualInt <=17
    noite = horarioAtualInt >=18 and horarioAtualInt <= 23

    if manhã:
        print('Bom dia')

    elif tarde:
        print('Boa Tarde')

    elif noite:
        print('Boa noite')

    else:
        print('Horário inválido')
except:
    print('caracteres inválidos')



'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande.
'''

firstname = input('What is your first name? ')

qntLname = len(firstname)

if firstname.isdigit() is not True:

    if qntLname <= 4:
        print('Seu nome é curto.')
    elif qntLname >4 and qntLname <= 6:
        print('Seu nome é normal')
    elif qntLname > 6:
        print('Seu nome é muito grande')

else:
    print('Caracteres inválido')




   