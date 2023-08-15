'''
        Execicios com Function
        
1 - Criar uma function que faça uma
multiplicação com todos os argumentos
não nomeados.
Retorne o valor para um variavel e
mostre o valor da variavel

2 - Criar uma function que fala se
o numero e impar ou par.
Retorne se o numero e par ou impar.
'''
#-----------------///--------------------///---------------------///
#                   Exercicio 1
def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
        
numero = 1,2,3,4,5,6,7,8,9,
multiplicacao_numeros = multiplicacao(*numero)
print(multiplicacao_numeros)

'''
# numeros_digitados = 0
# lista_numeros = []
# indice = 0
# numeros = ()
# while indice < 10:
#     numeros_digitados = input('Digite um numero: ')
#     lista_numeros.append(numeros_digitados)
#     indice += 1
#     print(lista_numeros)
# for numero in lista_numeros:
#     numero += tuple(lista_numeros)
#     print(numero)
'''
#-----------------///--------------------///---------------------///
print('-' * 95)
#-----------------///--------------------///---------------------///
#                   Exercicio 2


def par_impar(x):
    multiplo_de_dois = x % 2 == 0
    if multiplo_de_dois:
       return(f'O valor {x} é par!!')
  
    return(f'O valor {x} é impar')


print(par_impar(11))
print(par_impar(12))
print(par_impar(16))
print(par_impar(110))   

    
    