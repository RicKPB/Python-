"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7


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

#Neste exemplo do execicio final sobre a secao Introducao a Python, mostra um gerador para conferir se o cpf que o usuario passar é valido ou não.

#----------//--------------------//------------------//---------------//
#              PRIMEIRO DIGITO CPF
CPF = '74682489070'
nove_digitos = CPF[:9]

indice_multiplicacao_1 = 10
lista_valores = []

for digito_cpf in nove_digitos: 
    valor_cpf = int(digito_cpf) * indice_multiplicacao_1
    indice_multiplicacao_1 -= 1
    lista_valores.append(valor_cpf)
          
soma_primeiro_digito = 0
for digito_soma in lista_valores:
    soma_primeiro_digito += digito_soma
       
digito_1 = ((soma_primeiro_digito * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0
print(f'O primeiro digito do cpf ė: {digito_1}')

#----------//--------------------//------------------//---------------//
#             SEGUNDO DIGITO CPF

dez_digito = nove_digitos + str(digito_1)
indice_multiplicacao_2 = 11

soma_segundo_digito = 0
for digito in dez_digito:
    soma_segundo_digito += int(digito) * indice_multiplicacao_2
    indice_multiplicacao_2 -= 1

digito_2 = (soma_segundo_digito * 11) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

print(f'O segundo digito do cpf é: {digito_2}')

cpf_gerado_sistema = (f'{nove_digitos}{digito_1}{digito_2}')
if CPF == cpf_gerado_sistema:
    print(f'{cpf_gerado_sistema} é um CPF valido.')
else:
    print('CPF invalido')
    





