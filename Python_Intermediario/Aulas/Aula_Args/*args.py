'''
args -> Argumentos não nomeados
* - *args (desempacotamento e empacotamento)
'''

#-----------------///--------------------///---------------------///
#                  LEMBRESSE DESEMPACOTAMENTO

x, y, *resto = 1,2,3,4
print(x, y, resto)
#    X e Y (Desemoacotamento) *resto (Empacotamento)
#-----------------///--------------------///---------------------///
print('-' * 95)
#-----------------///--------------------///---------------------///
#                  *args (Empacotamento em Function)

def soma(*args):
    #print(args, type(args))
    total = 0
    for numero in args:
        total+= numero
    return total
    
soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)
#-----------------///--------------------///---------------------///
print('-' * 95)
#-----------------///--------------------///---------------------///
#                  FUNCTION SUM()

#Isso e uma funcao igual aq ue nos fizemos no exemplo de *args logo acima.
print(sum((1,2423,631,56436,213,6,72)))
#-----------------///--------------------///---------------------///
print('-' * 95)
#-----------------///--------------------///---------------------///
#                  ENVIAR UM PACOTE PARA UMA FUNCTION

def somas(*args):
    #print(args, type(args))
    total = 0
    for numero in args:
        total+= numero
    return total

numeros= 1,2423,631,56436,213,6,72
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))
# print(*numeros)
