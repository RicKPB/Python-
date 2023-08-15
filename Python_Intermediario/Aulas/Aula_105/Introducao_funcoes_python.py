'''
Introducao a funcoes (def) em Python.
Funcoes sao trechos de codigo usados para
replicar determinada acao durante seu codigo.
Ela podem receber valores para parametros (argumentos)
e retornar um valor especifico.
Por padrao funcoes Python retornam valor none (nada).

'''

#-----------------///--------------------///---------------------///
#                   CRIAR UMA FUNCAO
def imprimir():
    print('Varias vezes pode se reutilizar!!!')

imprimir()
#-----------------///--------------------///---------------------///
print('-' * 95)
#-----------------///--------------------///---------------------///
#                   DEFININDO ARGUMENTOS


#             (VARIAVEIS)
def argumentos(a, b, c):
    print(a, b, c)#mostrando os valores que foi passado para as variaveis
    
#         (VALORES DAS VARIAVEIS)    
argumentos(1, 2, 3)
argumentos(4, 5, 6)
#-----------------///--------------------///---------------------///
print('-' * 95)
#-----------------///--------------------///---------------------///

def saudacao(nome='Sem nome'):
    print(f'Ola, {nome}')

saudacao('Henrique')
saudacao('Joao')
saudacao()

