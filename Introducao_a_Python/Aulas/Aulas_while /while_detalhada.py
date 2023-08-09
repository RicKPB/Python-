'''
Repetição
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

break -> o break serve para poder finalizar o while aonde ele finaliza e continua o programa 

Quando o while é False ele deixa grifado alinha de codigo que não roda no sistema pois aquele while é False.
'''

while False:
    print('Não roda!!!!')
    
print('Roda')

print('-' * 95)

contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)