# Operadores lógicos 
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São cosiderados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é 
# usado para representar um não valor 

'''
entrada = input('Deseja [E]ntrar ou [S]air ? ').lower()

if entrada == 's':
    print('saindo...')
 
senhaDigitada = input('Digite sua senha:')
senhaPermitida = 'senha123'


if entrada == 'e' and senhaDigitada == senhaPermitida:
    print('Entrando...')

elif senhaDigitada != senhaPermitida:
    print('Senha invalida')
'''
# Avaliação de curto circuito


senha = input('Digite senha: ') or 'Argumento invalido'
print(senha)
