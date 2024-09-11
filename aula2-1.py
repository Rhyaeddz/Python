# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser True
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele Valor 
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado
# para representar um não valor 


entrada = input('Deseja [E]ntrar ou [S]air ? ').lower()

if entrada == 's':
    print('saindo...')
 
senhaDigitada = input('Digite sua senha:')
senhaPermitida = 'senha123'


if entrada == 'e' and senhaDigitada == senhaPermitida:
    print('Entrando...')

elif senhaDigitada != senhaPermitida:
    print('Senha invalida')

# avaliação de curto circuito
# print(True and True and True)
