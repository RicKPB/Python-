"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# Se no caso nos formos copiar uma lista para outra lista, criando duas lista, se voce colocar como se lista_b = list_a ele recebera os valores da lista a e se houver uma alteracao na lista a ele altera na b tambem.

# No caso de usar a funcao .copy, list_b = list_a.copy(), ele cria dentro do sistema a lista b com os valores da list a so que se for alterado dentro da lista a os valores da lista b nao serao alterados.

list_a = ['Henrique', 'joao', 'gordao']
list_b = list_a.copy()

list_a[0] = 15
print(list_a)
print(list_b)