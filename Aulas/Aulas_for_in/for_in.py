'''
Repetição
For 

Diferente de while nao precisa fazer indice para contador.
Break, Continue else tudo se funciona no for do mesmo jeito que se funciona no while.
Diferenca entre while e for:
        while -> usado para coisa aonde nos nao sabemos o tamanho.
        for -> mais usado para codigos que nos sabemos o comeco e o fim.
'''

texto = 'Python'

novo_texto = ''

for letra in texto:
    novo_texto += f'${letra}'
    print(letra)
print(novo_texto + '$')