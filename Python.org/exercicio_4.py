#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def testeNum(*args):

    valor =  int(input('Digite um valor: '))

    if valor > 0:
        print('P')

    else:
        print('N')


testeNum()