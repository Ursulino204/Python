x = int(input('Primeiro Valor:'))
y = int(input('Segundo Valor: '))

if x > y:
    print('O Primeiro  ' + str(x) + '  é maior que o Segundo')
elif x < y:
    print('O Segundo  ' + str(y) + '  é maior que o Primeiro')
else:
    print('São iguais')