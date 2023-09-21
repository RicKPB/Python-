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