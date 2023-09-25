# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def quantidadeDigitos(*args):
    numero_digitado = int(input('Digite um numero: '))
    str_numero = str(numero_digitado)
    print (len(str_numero))
   
quantidadeDigitos()

