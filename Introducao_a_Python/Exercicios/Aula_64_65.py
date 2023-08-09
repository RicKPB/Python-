'''

Interando strings com while

'''

nome = 'Henrique'
nome_editado = ''

indice = 0

while indice < len(nome):
    letra = nome[indice]
    nome_editado += f'${letra}'
    indice += 1
#--------/----------/---------/

nome_editado += '$'
print(nome_editado)   
    