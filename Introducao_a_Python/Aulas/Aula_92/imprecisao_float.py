"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
<.https://en.wikipedia.org/wiki/Double-precision_floating-point_format.>
<.https://docs.python.org/pt-br/3/tutorial/floatingpoint.html.>
"""

import decimal

#---------/--------/--------/--------/--------/
#Primeiro metodo para formata o numero de ponto flutante.
numero_1 = 0.7
numero_2 = 0.1
soma = numero_1 + numero_2
#print(soma) = 0.79999999999...
print(f'{soma:.2f}')
#---------/--------/--------/--------/--------/
print('-' * 95)
#---------/--------/--------/--------/--------/
#Podemos utilizar a funcao round aonde passamos a variavel e no segundo argumento passamos o numero de casas decimais.
numero_4 = 0.7
numero_3 = 0.1
soma_1 = numero_4 + numero_3
print(round(soma, 2))
#---------/--------/--------/--------/--------/
print('-' * 95)
#---------/--------/--------/--------/--------/
#Tambem temos o .decimal que e importado de uma bibloteca aonde ele calcula numeros de ponto flutuante mais precisamente (utilizar em casos de numeros com ponto flutuante muito grandes), em casos como o exemplo abaixo ele mostra mais numeros do que o normal (se colocarmos o valor da class Decimal em str ele calcula precisamente).
num_1 = decimal.Decimal(0.1)
num_2 = decimal.Decimal(0.7)
valor = num_1 + num_2
print(valor)