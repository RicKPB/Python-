'''
Repetição
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

break -> o break serve para poder finalizar o while mais proximo dele aonde ele finaliza e continua o programa.

continue -> Faz com que ele volte ao while mais proximo dele, e nao mostra oque a condicao diz.
'''

quantidade_linha = 5
quantidade_colunas = 5


linha = 1

while linha <= quantidade_linha:
    coluna = 1
    while coluna <=quantidade_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
    

    