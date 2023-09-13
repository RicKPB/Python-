import re

#Utilizacao de metodo com expresao regular
cpf = re.sub(
    r'[^0-9]',
    '',
#aqui estamos definindo que queremos que substituir oque estiver entre 0 - 9 e que nao seja um numero (^) -> simbolo para oque nao for um num , aonde sera substituido para nada (str vazia)
    '746.824.890-70'
)



#----------//--------------------//------------------//---------------//
#              PRIMEIRO DIGITO CPF
# CPF = '746.824.890-70'\
#     .replace('.', '')\
#     .replace('-', '')\
#     .replace(' ', '')
    #O metodo replace serve de modo para apagar oque a gente deseja de um str.
nove_digitos = cpf[:9]

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
if cpf == cpf_gerado_sistema:
    print(f'{cpf_gerado_sistema} é um CPF valido.')
else:
    print('CPF invalido')
    
