'''
For + Range

Range -> range(start, stop , step)
***** -> ** inicio  final   quantos em quantos 

'''

#quando so colocar um valor esse sera colocado de start = 0 stop = valor que voce colocou e step = 1
'''numeros = range(10)'''

#nesse caso ja definimos o valor de strat = 5 e stop = 20. step = 1
'''numeros = range(5,20)'''

#no ultimo definimos os tres valores start = 5 stop = 20 e step = 2
numeros = range(5, 20, 2)

for numero in numeros:
    print(numero)