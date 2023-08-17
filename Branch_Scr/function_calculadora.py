

def calculadora(*args):
    
    while True:
        valor_um = input('Digite um valor: ')
        valor_dois = input('Digite mais um valor: ')
        operador = input('Digite o operador (+-/*): ')
    
        numero_valido = None
        valor_um_float = 0
        valor_dois_float = 0
        
        try:
            valor_um_float = float(valor_um)
            valor_dois_float = float(valor_dois)
            numero_valido = True
        
        except:
            numero_valido = None
            if numero_valido is None:
                print('Um dos valores nao e um valor valido!')
                continue
        
        operadores_validos = ('+-/*')
        
        if operador not in operadores_validos:
            print('O operador digitado nao e valido!!')
            continue
            
        if len(operador) > 1:
            print('Digite omente um operador!!')
            continue
        
        print('O resultado da conta esta logo abaixo confira!')
         
        if operador == '+':
            resultado = valor_um_float + valor_dois_float
            print(f'{valor_um_float} + {valor_dois_float} = ',resultado)
        
        elif operador == '-':
            resultado = valor_um_float - valor_dois_float
            print(f'{valor_um_float} - {valor_dois_float} = ',resultado)
        
        elif operador == '/':
            resultado = valor_um_float / valor_dois_float
            print(f'{valor_um_float} / {valor_dois_float} = ',resultado)
            
        elif operador == '*':
            resultado = valor_um_float * valor_dois_float
            print(f'{valor_um_float} * {valor_dois_float} = ',resultado)
            
        else:
            print('COMO CHEGOU AQUI ??????????')
        
        sair = input('Quer sair? [s]air ').lower().startswith('s')
        
        if sair is True:
            break
        


calculadora()
    
        
    
    