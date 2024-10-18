frase = 'aaaooo'

i = 0 

qndApareceuMaisVezes = 0
LetraApareceuMaisVezes =  ''

while i < len  (frase):
    letraAtual = frase[i]

    if letraAtual == ' ':
        i += 1
        continue 

    qtdApareceuMaisVezesAtual = frase.count(letraAtual)

    if qndApareceuMaisVezes < qtdApareceuMaisVezesAtual:
        qndApareceuMaisVezes = qtdApareceuMaisVezesAtual
        LetraApareceuMaisVezes  =  letraAtual

    i += 1

print('A letra que apareceu mais vezes foi '
       f'"{LetraApareceuMaisVezes}" que apareceu '
       f'{qndApareceuMaisVezes}x'
) 




