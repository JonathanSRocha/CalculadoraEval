print('=================================================')
print('Esse programa é uma calculadora para dois valores')
print('=================================================')
x = input('Digite o primeiro valor: ')
operador = input('Digite o operador(+,-,/,*,**,%): ')
y = input('Digite o segundo valor: ')
if x != '' and y != '':
    x = int(x)
    y = int(y)
else:
    print('Em uma das parcelas você não digitou nada.')

resultado = f'{x} {operador} {y}'

resultado_final = eval(resultado)

print(resultado_final)
