# Calculadora com while

while True:
    
    entrarOuSair = input('Deseja calcular um número? [S]im / [N]ão ')

    if entrarOuSair == 'S':

        PrimeiroNumero = input('Digite o primeiro número do cálculo: ')
        segundoNumero = input('Digite o segundo número do cálculo ')

        if PrimeiroNumero.isdigit and segundoNumero.isdigit() and operacao.len() is 1:

            operacao = input('Qual operação você deseja fazer entre os números? [+],[-],[*],[/].')

            floatPrimeiroNumero = float(PrimeiroNumero)
            floatSegundoNumero = float(segundoNumero)

            adicao = floatPrimeiroNumero + floatSegundoNumero
            subtracao = floatPrimeiroNumero - floatSegundoNumero
            multiplicacao = floatPrimeiroNumero * floatSegundoNumero
            divisao = floatPrimeiroNumero / floatSegundoNumero
            
            if operacao == '+':
                print(f'{floatPrimeiroNumero} mais {floatSegundoNumero} é igual á {adicao}.')
            elif operacao == '-':
                print(f'{floatPrimeiroNumero} menos {floatSegundoNumero} é igual á {subtracao}.')
            elif operacao == '*':
                print(f'{floatPrimeiroNumero} vezes {floatSegundoNumero} é igual á {multiplicacao}.')
            elif operacao == '/':
                print(f'{floatPrimeiroNumero} dividido por {floatSegundoNumero} é igual á {divisao}.')
        else:
            print('Um dos números ou operação estão incorretos !')
       
    elif entrarOuSair == 'N': 
        print('Saindo . . .')
        break
    else:
        print('Por favor digite apenas [S] Caso queira calcular um número ou [N] caso queira sair !')