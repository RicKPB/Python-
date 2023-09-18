"""
    Dicionarios em Python (type dict)
    Dicionarios sao estruturas de dados do tipo
    par e "chave" e "valor".
    Chaves podem ser consideradas  como o "indice"
    que vimos na lista e podem ser de tipo imutaveis 
    como: str, int, float, bool, tuple, etc.
    O valor pode ser de qualquer tipo, incluindo 
    outro dicionario.
    Usamos as chaves - {} - ou a classe dict para criar 
    dicionarios.
    Imutaveis: str, int, float, bool, tuple
    Mutavel: dict, list
    pessoa: {
        'nome': 'Henrique',
        'sobrenome': 'Papeschi',
        'idade': 18,
        'altura': 1.8,
        'endereços': [
            {'rua': 'tal tal', 'numero': 123},
            {'rua': 'outra rua', 'numero': 125}
        ]
    }
    print(pessoa, type(pessoa))
"""

#----------------------///-----------------------
#               CRIANDO DICIONARIO
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
print(pessoa, type(pessoa))

#----------//--------//---------//----------
print('-' * 95)
#----------//--------//---------//----------
#       ACESSAR SOMENTE UM VALOR DO DICIONARIO:

print(pessoa['nome'])
#print(dict[nome do valor])

#----------//--------//---------//----------
print('-' * 95)
#----------//--------//---------//----------
#       MESMO O DICT NAO SENDO INTERALVEL ATRAVES DO FOR IN PODEMOS ACESSAR CADA VALOR DO DICT

for chave in pessoa:
    print(chave, '-', pessoa[chave])

#----------//--------//---------//----------
print('-' * 95)
#----------//--------//---------//----------
#               METODO DICT

pessoa2 = dict(nome='Henrique', sobrenome='Miranda')

#----------//--------//---------//----------