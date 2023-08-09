'''
Repetição
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

break -> o break serve para poder finalizar o while mais proximo dele aonde ele finaliza e continua o programa.

continue -> Faz com que ele volte ao while mais proximo dele, e nao mostra oque a condicao diz.
'''

contador = 0

while contador < 100:
    contador += 1
    
    if contador == 6:
        print('Numero Pulado')
        continue
    
    if contador > 25 and contador <50:
        print('Numeros pulados 26 a 49')
        continue

    print(contador)
    
    if contador == 50:
        print('Parar loop')
        break
    
    
print('acabou')