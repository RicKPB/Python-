#Desempacotamento em chamadas
#Metodos e funcao

string = 'ABCD'
lista = ['Henrique', 'Joao', 'Gordao']
tupla = 'Python', 'é', 'legal.'

salas = [
    # 0       1
    ['Joao', 'Gordao'], # 0
    # 0
    ['Henrique'], # 1
    # 0        1      2      
    ['Lsete', 'Leo', 'ziole'], #2
]

# a, b, c = lista
# print(a, c)


#--------//-------------//-----------------//
# Interacao para pegar cada item da lista

#O print(*lista) faz a mesma coisa que o for.

# for nome in lista:
#     print(nome, end=' ', sep=' ')
    
print(*lista)
print(*string)
print(*tupla)
print(*salas, sep='\n')
#--------//-------------//-----------------//
print('-' * 95)
#--------//-------------//-----------------//