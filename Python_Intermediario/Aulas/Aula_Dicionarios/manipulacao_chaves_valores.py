#   Manipulando chaves e valores em dicionarios

pessoa = {
        'nome': 'Henrique',
        'sobrenome': 'Papeschi',
        'idade': 18,
        'altura': 1.8,
        'endereços': [
            {'rua': 'tal tal', 'numero': 123},
            {'rua': 'outra rua', 'numero': 125}
        ]
    }

pessoa['numero'] = '123456789'
#adcionando chave ao um dict
print(pessoa)

#adicionando chaves dinamicamente
chave = 'nome_completo'
pessoa[chave] = 'Henrique Papeschi Bernardo'

#excluindo uma chave
del pessoa['numero']

#acessando uma chave que nao existe
print(pessoa.get('numero'))
#se caso a chave nao existir ele retorna um valor None, se caso existir ele retorna o valor da chave.

#no caso da utilizacao do if so funcionara com o metodo .get (aconselhado a usar com is none)
if pessoa.get('numero1') is None:
    print('Nao existe!!!')
else:
    print(pessoa['numero1'])

print(pessoa)
#print(pessoa['nome1'])
#neste caso ocasiona no erro KeyError aonde mostra como definido o nome de chave pro dict [chave = key]