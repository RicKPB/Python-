'''
Enumerate -> enumera interaveis(indices)
'''

nomes = ['Henrique', 'Felipe', 'Sid']

lista_enumerada = enumerate(nomes)

for indice, nome in lista_enumerada:
    print(indice, nome)