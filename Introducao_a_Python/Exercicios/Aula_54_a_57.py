"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero_digitado = input('Digite um numero: ')
# resto = None

# try:
#     numero_int = int(numero_digitado)
#     resto = numero_int % 2
    
#     if resto == 0:
#         print(f'O numero {numero_int} é um numero par')
    
#     else:
#         print(f'O numero {numero_int} é um numero impar')
    

# except:
#     print(f'O numero que você informou não e um numero inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# entrada_horario = input('Digite o horario em numeros inteiros: ')

# try: 
#     hora_int = int(entrada_horario)
    
#     if hora_int >= 0 and hora_int <= 11:
#         print(f'Bom Dia {hora_int}')
    
#     elif hora_int >=12 and hora_int <=17:
#         print(f'Boa Tarde {hora_int}')
        
#     elif hora_int >=18 and hora_int <= 23:
#         print(f'Boa Noite {hora_int}')
        
#     else:
#         print('Não reconheço esse horario')

# except:
#     print('Você não digitou um numero inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_usuario = input('Digite seu nome: ')
quantidade_letras = len(nome_usuario)
   
if quantidade_letras > 1:
    
    if quantidade_letras <= 4:
        print('Seu nome é curto')
    
    elif quantidade_letras >= 5 and quantidade_letras <= 6:
        print('O seu nome é normal')
    
    else:
        print('O seu nome e grande')
        
else:
    print('Voce nao digitou um nome')