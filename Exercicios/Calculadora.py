'''
Mesmo execicio da aula 66 a 68 so que aqui foi feito sem ver a aula e sem acompanha o codigo para poder treinar while
'''

while True:
    numero_um = input('Digite um numero: ')
    numero_dois = input('Digite outro numero: ')
    operador = input('Digite o operador desejado: ')
    
    numero_valido = None
    numero_um_float = 0
    numero_dois_float = 0
    
    try:
        numero_um_float = float(numero_um)
        numero_dois_float = float(numero_dois)
        numero_valido = True
        
    except:
        numero_valido = None
        if numero_valido is None:
            print('Um ou ambos dos numeros digitados e invalido!!')
            continue
    
    operador_validos = '+ - / *'
    
    if operador not in operador_validos:
        print('Operador digitado nao e valido!!')
        continue
    
    if len(operador) > 1:
        print('Voce so pode digitar um operador')
        continue
    
    if operador == '+':
        print(f'{numero_um_float} + {numero_dois_float} = ',numero_um_float + numero_dois_float )
        
    elif operador == '-':
        print(f'{numero_um_float} - {numero_dois_float} = ',numero_um_float - numero_dois_float ) 
    
    elif operador == '*':
        print(f'{numero_um_float} * {numero_dois_float} = ',numero_um_float * numero_dois_float )  
        
    elif operador == '/':
        print(f'{numero_um_float} / {numero_dois_float} = ',numero_um_float / numero_dois_float ) 
        
    else:
        print('Se voce chegou aqui algo de errado esat no codigo!!')  
    
    #------------------------/////--------------------------------------
    sair = input('Quer sair? [s]air: ').lower().startswith('s')
    if sair is True:
        print('Sistema finalizado!')
        break