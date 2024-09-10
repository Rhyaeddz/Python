a = 'Aaaa'
b = 'B'
c = 1.1

# 'parametro' é nome= dps do '=' vem o argumento

string = 'a={nome1} b={nome2} c={nome3:.2f} {nome3:.2f}' 

formato = string.format(nome1=a, nome2=b, nome3=c )


print(formato)