'''
whille == for
'''

for i in range(9):
    if i == 2:
        print('i e 2, pulando...')
        continue
    
    if i == 8:
        print('i e 8, seu else nao executara')
        break
    
    for j in range(1, 3):
        print(i, j)
        
else:
    print('For completo com sucesso')
    


