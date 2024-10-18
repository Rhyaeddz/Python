'''
Exercicío
Peça ao usuário para digitar seu nome 
Peça ao usuário para digitar sua idade
Se o nome e a idade forem digitados:
    Exiba:
        seu nome é {nome}
        seu nome invertido é {nome invertido}
        se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba 'desculpe, você deixou campos vazios."

'''
usuaryName = input('Insira o seu nome: ')
usuaryAge = input('Insira sua idade:  ')
nomeEspaços = usuaryName.count(' ')
nLetrasNome = (len(usuaryName) ) - nomeEspaços

if usuaryName and usuaryAge != ' ':

    print(f'Seu nome é:{usuaryName}')
    print(f'Você tem {usuaryAge} anos.')
    print(f'Seu nome invertido é:',usuaryName[::-1])

    if nomeEspaços == 0:
        print(f'Seu nome não tem nenhum espaço e contém {nLetrasNome} letras.')
    else:
        print(f'Seu nome tem {nomeEspaços} espaços e contém {nLetrasNome} letras.')

    print(f'A primeira letra do seu nome é {usuaryName[0]} e a última é {usuaryName[-1]}.')

else:     
    print(f'Desculpe, você deixou os campos vazios.')





