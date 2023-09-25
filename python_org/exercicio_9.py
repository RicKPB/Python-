# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.


def numeroReverso(*args):

    numero = int(input('Digite um numero: '))
    str_numero = str(numero) 

    print(str_numero[::-1])

numeroReverso()