'''
High Order Functions
Funcao de primeira classe

Nos podemos passar funcoes como argumentos para outras funcoes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

!!Aula meio confusa rever alguns dias depois!!
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def execucao(funcao, *args):
    return funcao(*args)


print(
    execucao(saudacao, 'Bom Dia', 'Henrique')
)