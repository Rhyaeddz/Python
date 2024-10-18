'''
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''

qtdLinhas = 5
qtdColunas = 5

linha = 1
while linha <= qtdLinhas:
    coluna = 1
    while coluna <=qtdColunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1