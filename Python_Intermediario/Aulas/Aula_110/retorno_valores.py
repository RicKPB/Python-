'''
Retorno de valores da Function(return)


Existem funcoes como o print que nao precisam retornar valores (none),
e existem "funcoes" que retornam valores.

Nao e possivel continuar um codigo depois do return pois ele indica ao Python que ele deve para oque ele ta fazendo e e retonar aquele valor.
'''

#-----------------///--------------------///---------------------///
#                   PRINT IS NONE (TRUE)

#A Function print ele e utilizada como se retornasse um não-valor, ela foi criada so para pode jogar coisas para saida do sistema, mostrar algo na tela.
#PRINT UMA FUNCTION QUE EXIBE UM VALOR E NÃO TEM VALOR.   
variavel = print('Henrique')
#variavel = None
print(variavel is None)
#-----------------///--------------------///---------------------///
print('-' * 95)
#-----------------///--------------------///---------------------///
#                   RETURN

def soma(x, y):
    #print(x + y) 
    #Para com que a funcao retorne um valor deve ser usada return aonde ele retorna um valor para a funcao.
    return x + y
    print(1+1)
    #Nao sera executado
    

#Neste caso ocorrera um erro de NoneType, pois quando jogado na variavel a funcao retorna None
soma1 = soma(2,2)
soma2 = soma(3,3)
print(soma1 + soma2)
#Usando o return podemos ver que as variaveis tiveram seus valores e foi corrigido uo erro (NoneType)
#-----------------///--------------------///---------------------///
print('-' * 95)
#-----------------///--------------------///---------------------///
#                   TESTE RETURN

def multipla(x, y):
    if x < 10:
        return 10, 20
    return (x + y)

soma1 = multipla(11, 11)
soma2 = multipla(15, 2)
print(soma1)
print(soma2)
print(multipla(9, 11))


