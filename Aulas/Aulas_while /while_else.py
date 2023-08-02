''' While/Else '''

'''
Nesse caso podemos ver que o else foi executado mesmo com o while sendo feito inteiro
'''
str = 'Valor Qualquer'

i = 0

while i < len(str):
    letra = str[i]
    
    print(letra)
    i += 1
    
else:
    print('O else foi executado')
    
print('O else nao foi executado')


'''
So que se no caso houver um break no meio do while o else nao sera executado.
'''

#No caso de nao houver espaco na str o else sera executado e isso pode ser utilizado dai para fazer o codigo no caso de nao houver espaco na str

str = 'Valor Qualquer'

i = 0

while i < len(str):
    letra = str[i]
    
    if letra == ' ':
        break
    
    print(letra)
    i += 1
else:
    print('O else foi executado')
    
print('O else nao foi executado')