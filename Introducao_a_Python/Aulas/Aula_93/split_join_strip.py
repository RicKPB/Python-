'''
split e join com list e str,
split - divide uma str, (list)
join - une uma string
'''
#---------/--------/--------/--------/--------/
#                   SPLIT

frase = '     Olha so que,     coisa interessante.      '
lista_palavras_cruas = frase.split(',')
lista_frase = []

#Metodo usando for para formata palaras de lista com indice.
for i, frase in enumerate(lista_palavras_cruas):
    lista_frase.append(lista_palavras_cruas[i].strip())

print(lista_frase)
print(lista_palavras_cruas)

#---------/--------/--------/--------/--------/
print('-' * 95)
#---------/--------/--------/--------/--------/
#                   JOIN
# Somente listas tuplas e str que sao itens iteraveis
letras_unidas = '-'.join('abc')
print(letras_unidas)

frase_lista_unida = '-'.join(lista_frase)
print(frase_lista_unida)
