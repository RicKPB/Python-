'''
Repetição
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

break -> o break serve para poder finalizar o while aonde ele finaliza e continua o programa 

'''

condicao = True

print('No caso de querer parar o sistema digite sair')

while condicao:
    str_chave = input('Digite algo para chave: ')
    print(str_chave)
    
    if str_chave == 'sair':
        break
    
print(123)



'''

Loop infinito -> Quando o codigo nao tem fim

condicao = True

while condicao:
    print(1)
    print(2)
    print(3)
'''