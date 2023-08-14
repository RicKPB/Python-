import random

def gerador_num(
    lista_inteiro = [None],
    lista_float = [None],
    numero_digitado = ''
    
):
    for indice in range(10):
        numero_digitado += str(random.random()) 
        
        if '.' in numero_digitado:
            numero_float = (numero_digitado)
            print(f'Float = {numero_float}')
            lista_float.append(numero_float)
           
              
    
        else:
            numero_int = (numero_digitado)
            print(f'Int {numero_int}')
            lista_inteiro.append(numero_int)
           
        
    lista_inteiro.pop(0)
    lista_float.pop(0)
    print(f'Lista Float:\n \
        {lista_float}'
    )
    print(f'Lista Inteiro:\n \
          {lista_inteiro}'
    )
    


gerador_num()
   
        