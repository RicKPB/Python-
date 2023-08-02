'''
Execicio para ver qual letra que se repetiu mais vezes.

Caso tenha empatado duas letras em mais quantidade ele mostra a que se apareceu primeiro 

'''


frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum. '
    
i = 0
letra_apareceu_mais_vezes = ''
quantidade_apareceu_mais_vezes = 0 
while i < len(frase):
    letra_atual = frase[i]
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if quantidade_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        quantidade_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
    
    
    i += 1
    
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu ' 
    f'{quantidade_apareceu_mais_vezes}x'      
)