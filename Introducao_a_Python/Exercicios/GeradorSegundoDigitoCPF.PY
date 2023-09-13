"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

# Resolucao do exercicio do gerador do segundo digito do cpf, feito sem auxilio de aula ou codigo feito

CPF = [7,4,6,8,2,4,8,9,0,7,0]
nove_digitos = CPF[:10]

indice_multiplicacao = 11
lista_valores = []


for digito_cpf in nove_digitos: 
    valor_cpf = digito_cpf * indice_multiplicacao
    indice_multiplicacao -= 1
    lista_valores.append(valor_cpf)
        
# print(lista_valores) 
# [77, 40, 54, 64, 14, 24, 40, 36, 0, 14]
    
resultado_soma_cpf = 0
for digito_soma in lista_valores:
    resultado_soma_cpf += digito_soma
       
# print(resultado_soma_cpf)
# 

digito = ((resultado_soma_cpf * 10) % 11)
digito = digito if digito <= 9 else 0
print(f'O primeiro digito do cpf ė: {digito}')

# print((resultado_soma_cpf * 10) % 11)
#
