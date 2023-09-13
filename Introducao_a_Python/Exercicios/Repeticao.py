'''
Mesmo execicio da aula 70 e 71 so que aqui foi feito sem ver a aula e sem acompanha o codigo para poder treinar while
'''

frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum. '
    
i = 0
qtd_apareceu_mais_vezes = 0 
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_letra_atual= frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if qtd_apareceu_mais_vezes < qtd_letra_atual:
        qtd_apareceu_mais_vezes = qtd_letra_atual
        letra_apareceu_mais_vezes = letra_atual
     
    i += 1
    
print(
    f'A letra que mais apareceu foi "{letra_apareceu_mais_vezes}" que foi {qtd_apareceu_mais_vezes}X'
)