'''
Mesmo execicio da aula 90 e 91 so que feito sem auxilio de aula ou codigo feito.
'''

import os
lista_compras = []

while True:
    
    possibilidades_lista = input(
        'Selecione uma opção:\n'
        '[i]nserir [a]pagar [l]istar '  
        ).lower()
    
    
    
    if possibilidades_lista == 'i':
        os.system('cls')
        item_lista = input('Valor: ')
        lista_compras.append(item_lista)
       
    
    elif possibilidades_lista == 'a':
        os.system('cls')
        indice_str = input('Escolha o indice a apagar: ')
        
        try:
            indice = int(indice_str)
            del lista_compras[indice]
        
        except IndexError and TypeError:
            print('Não foi possivel apagar esse indice!')
    
    elif possibilidades_lista == 'l':
        os.system('clear')
        if len(lista_compras) == 0:
            print('Não ah nenhum item na lista!')
        for indice, item_lista in enumerate(lista_compras):
            
            print(indice, item_lista)
       
    
    else:     
        break