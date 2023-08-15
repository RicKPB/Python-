'''
Escopo de funcoes em Python
Escopo siginifica o local aonde aquele codigo pode atingir.
Existe o Escopo Global e o Local;
O Escopo Global é o escopo onde todo o codigo e alcançavel.
O Escopo Local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos iternos nos escopos externos.
A palavra global faz com que uma variavel do escopo externo 
tenha o mesmo valor do escopo interno.

Escopo -> Oque é definido dentro da função fica protegido, fica no escopo da função.
'''

#-----------------///--------------------///---------------------///
#                   ESCOPO INTERNO                   
def escopo():
    x = 1
    print(x)
    
escopo()
# print(x) : Não era possivel fazer consulta pois esta dentro da função.
#-----------------///--------------------///---------------------///
print('-' * 95)
#-----------------///--------------------///---------------------///
#                   ESCOPO EXTERNO

# Nesse caso nos vamos definir o x no escopo do codigo e fazer a função ler o valor de x.

x = 1

def escopoEx():
    print(x)
    
escopoEx()
#-----------------///--------------------///---------------------///
print('-' * 95)
#-----------------///--------------------///---------------------///
#                   FUNÇÃO DENTRO DE FUNÇÃO
x = 1

def fuction():
    global x
    #Neste caso estamos manipulando o valor de x global ou seja depois de ser executada a function o valor do escopo global nao sera mais de 1 e sim sera o valor 10 pois estamos manipulando o valor dela.
    x = 10
    #Percebemos que aqui foi definido o valor de x no escopo interno da function aonde quando for executado a fuction o valor de x sera 10.
    def outraFunction():
        x = 11
        #Aqui esta sendo trocado para x = 11 dentro do escopo da outraFunction aonde quando executada sera mostrada o valor 11 e na function por fora sera mostrada 10.
        y = 2
        print(f'{x=}',f'{y=}')
    outraFunction()
    print(x)
 
print(x) 
#Neste caso sera mostrado o valor de x do escopo do modulo que seria o escopo global.(Sem manipulação) 
fuction()
print(x)
#Realizado a manipulação colocando o valor de x = 10 
    