"""
    Metodos uteis dos dicionarios em Python
    len - quantas chaves
    keys - iteravel com as chaves 
    values - iteravel com os valores 
    items - iteravel com chaves e valores
    setdefault - adiciona valor a chave se a chave nao existir 
    copy - retorna uma copia rasa (shallow copy)
    get - obtem uma chave 
    pop - apaga um item com a chave especifica (del)
    popitem - apaga o ultimo item adicionado 
    update - atualiza um dicionario com outro
"""

import copy

pessoa = {
        'nome': 'Henrique',
        'sobrenome': 'Papeschi',
    }

#----------//--------//---------//----------
print('-' * 95)
#----------//--------//---------//----------
#               LEN

print(len(pessoa)) 

#Podemos usar tbm o metodo print(pessoa.__len__()) -- dunder len

#----------//--------//---------//----------
print('-' * 95)
#----------//--------//---------//----------
#               KEYS

print(pessoa.keys())
#Nesta forma ele me entrega um dict keys, aonde podemos fazer uma coercao das chaves
# dict_keys, dict_itens, dict_values
print(tuple(pessoa.keys()))
print(list(pessoa.keys()))

#Outro metodo de pegar as chaves
for chave in pessoa:
    print(chave)

#----------//--------//---------//----------
print('-' * 95)
#----------//--------//---------//----------
#               VALUES

print(pessoa.values())
#Nesta forma ele me entrega um dict values, aonde podemos fazer uma coercao dos valores
# dict_keys, dict_itens, dict_values
print(tuple(pessoa.values()))
print(list(pessoa.values()))

#Outro metodo de pegar as values
for valor in pessoa.values():
    print(valor)

#----------//--------//---------//----------
print('-' * 95)
#----------//--------//---------//----------
#               ITEMS

#Nesta forma ele me entrega um dict_items, mostrando a chave e o valor como se fosse dentro de uma lista 
print(pessoa.items())

#Coercao
print(tuple(pessoa.items()))
print(list(pessoa.items()))

#Outro metodo de pegar os items
for chave, valor in pessoa.items():
    print(chave, valor)

#----------//--------//---------//----------
print('-' * 95)
#----------//--------//---------//----------
#               SETDEFAULT

#O metodo setdefault faz com que se voce fizer um print,
# de uma chave que nao existe ele cria a chave e da um valor,
# que voce deseja a ela, e se a chave existir o setdefault,
# nao se realiza.

print(pessoa)
pessoa.setdefault('idade', 0)
print(pessoa)

#----------//--------//---------//----------
print('-' * 95)
#----------//--------//---------//----------
#               SINAL DE ATRIBUICAO

d1 = {
    'c1': 1,
    'c2': 2,
}
#No caso de valores mutaveis como dict, ele nao realiza uma copia, e sim realiza um apontamento para o d1.
d2 = d1

print(d1)

#Entao no caso de fizer uma alteracao na d2 ele modifica o valor da d1 
d2['c1'] = 1000

print(d1)

#----------//--------//---------//----------
print('-' * 95)
#----------//--------//---------//----------
#               SHALLOW COPY

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}
#Na utilizacao do metodo .copy() (shallow copy), ele realiza uma copia para d2 do dict d1.
d2 = d1.copy()

#Com isso se realizarmos uma alteracao no dict d2, d1 nao sera afetada.
d2['c1'] = 1000

print(d1)
print(d2)

#Em caso de ouver valores mutaveis dentro do dict, ele vai fazer com que o dict aponte pra mesma lista na memoria
#Entao se no caso alterarmos na b2 um indice da lista o valor sera alterado nos dois dict(d1, d2)

d2['l1'][1] = 15

#No caso de querer realizar uma copia profunda do dict teremos que usar o import copy, que dentro dele existe o metedo copy.deepcopy()

d3 = copy.deepcopy(d1)

d3['l1'][1] = 99999

print('-' * 95)

print(d1)
print(d2)
print(d3)
#----------//--------//---------//----------
print('-' * 95)
#----------//--------//---------//----------
#               SHALLOW COPY