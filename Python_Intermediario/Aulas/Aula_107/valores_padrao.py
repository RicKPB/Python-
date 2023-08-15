'''
Valores padrao para parametros
Ao definir uma funcao, os parametros podem ter
valores padrao. Caso o valor nao seja 
enviado para o parametro, o valor padrao
sera usado.
Refatorar -> Editar o seu codigo.


|||!!!!!|||
Todo parametro que tem um valor padrao, o proximo parametro e obrigatorio a ter um valor padrao tambem.
'''


#-----------------///--------------------///---------------------///
#                   DEFININDO NAO VALORES (NONE)

# Quando definirmos um parametro com o valor = 0, ele e considerado um valor False, e nao mostra o valor se for colocado por exemplo em um if pois ele confronta como um bool:

def soma(x, y, z = 0):
    if z:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=} ', x + y )
    
soma(1, 3, 0)
#-----------------///--------------------///---------------------///
print('-' * 95)
#-----------------///--------------------///---------------------///
# Para fazermos com que o nao valor que foi colocado ser considerado para a soma podemos usar o is not

def soma_2(x, y, z = None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=} ', x + y )   

soma_2(7, 3, 0)           
