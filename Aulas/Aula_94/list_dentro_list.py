'''
List de list e seus indices

'''

salas = [
    # 0       1
    ['Joao', 'Gordao'], # 0
    # 0
    ['Henrique'], # 1
    # 0        1      2        3 
    ['Lsete', 'Leo', 'ziole', (0, 10, 20, 30, 40)], #2
]

for salas in salas:
    print(f'A sala e {salas}')
    for aluno in salas:
        print(aluno)


# try:
#     print(salas[2][2])
#     print(salas[2][3])
#     print(salas[2][3][3])
    
# except IndexError:
#     print('Indice nao existe')