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
"""

# Resolucao do exercicio do gerador do primeiro digito do cpf, feito sem auxilio de aula ou codigo feito

CPF = [7,4,6,8,2,4,8,9,0,7,0]
nove_digitos = CPF[:9]

indice_multiplicacao = 10
lista_valores = []


for digito_cpf in nove_digitos: 
    valor_cpf = digito_cpf * indice_multiplicacao
    indice_multiplicacao -= 1
    lista_valores.append(valor_cpf)
        
# print(lista_valores) 
# [70, 36, 48, 56, 12, 20, 32, 27]
    
resultado_soma_cpf = 0
for digito_soma in lista_valores:
    resultado_soma_cpf += digito_soma
       
# print(resultado_soma_cpf)
# 301

digito = ((resultado_soma_cpf * 10) % 11)
digito = digito if digito <= 9 else 0
print(f'O primeiro digito do cpf ė: {digito}')

# print((resultado_soma_cpf * 10) % 11)
#7


    
       

    
