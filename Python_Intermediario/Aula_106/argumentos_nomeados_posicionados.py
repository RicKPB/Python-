'''
Argumentos nomeados e nao nomeados em Python
Argumentos nomeados tem o nome com o sinal de '=' (variavel = valor)
Argumentos nao nomeados recebe apenas o argumento (valor)

'''

#-----------------///--------------------///---------------------///

def soma(x, y):
    print(f'{x=} y={y}', '|' ,'x + y = ', x + y )

soma(1, 2)
soma(2, 1)
soma(y=2 ,x=1)