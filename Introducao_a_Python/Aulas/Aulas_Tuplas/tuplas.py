'''
Tipo tupla - uma lista imutavel
'''

# Tuplas sao criadas no lugar de list que nao serao alteradas.

''' 
    Forma de criar tupla:
        Criar sem os conchetes -> tupla = 'marcos', 'felipe', ....
        Criar usando parentes -> tupla = ('Henrique', 'Felipe', 'Sid')
'''

nomes = ['Henrique', 'Felipe', 'Sid']
nomes = tuple(nomes) #conversao de list para tuple
print(nomes)



