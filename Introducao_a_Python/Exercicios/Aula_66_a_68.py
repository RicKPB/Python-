'''
Calculadora com while

Na aula foi passado que seria melhor ser feito tudo numa linha sobre a variavel sair pois, nela estamos dando uma variavel do tipo str so que quando usado o metodo 
.startswith ele converte ela para um bool. (Part. Finalizar)
'''


while True:
    
    #-----------------Valores e Conferencia deles----------------------
    numero_um = input('Digite o valor: ')
    numero_dois = input('Digite outro valor: ')
    operador = input('Digite o operador (+-/*): ')
    
    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0
    try:
        numero_1_float = float(numero_um)
        numero_2_float = float(numero_dois)
        numeros_validos = True
    except:
        numeros_validos = None
        if numeros_validos is None:
            print('Um ou ambos dos numeros nao sao validos!')
            continue
    
    operadores_permitidos = ('+-/*')
    
    if operador not in operadores_permitidos:
        print('O operador digitado nao e valido!')
        continue
    
    if len(operador) > 1:
        print('Digite somente um operador!')
        continue
    
    #------------------Contas e resultados----------------------
    
    print('Realizando sua conta, confira o resultdo abaixo!')
    
    if operador == '+':
        print(numero_1_float + numero_2_float)
    
    elif operador == '-': 
        print(numero_1_float - numero_2_float)   
    
    elif operador == '/': 
        print(numero_1_float / numero_2_float)
        
    elif operador == '*':     
        print(numero_1_float * numero_2_float)
    
    else:
        print('Algo deu errado pois nao era pra chegar aqui!!!')
    
    #------------------Finalizar----------------------
    sair = input('Quer sair? [s]air: ').lower().startswith('s')
   
    if sair is True:
        break
    
    
    
