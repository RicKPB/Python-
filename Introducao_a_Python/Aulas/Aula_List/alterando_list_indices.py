'''
Lista em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo,
Conhecimentos reutilizaveis -indices e fatiamentos.
Metodos uteis:
        append -> Adicionar item ao final da list
        insert -> Adicionar um item ao indice escolhido
        pop    -> Remove ou no final ou pelo indice da list
        del    -> Apaga um indice
        clear  -> Limpa a list
        extend -> Estede a list
        +      -> Concatena a list

Create Read Update   Delete
Criar, Ler, Alterar, Apagar = list[i] (CRUD)

Evitar de mexer no comeco e no meio da lista,
Melhor trabalhar no final da lista
'''

#---------/--------/--------/--------/--------/
#                     DEL
# Quando utilizarmos para apagar o ultimo item da lista e nos nao sabemos o ultimo indice da lista pode usar o indice negativo (-1) que ele representa o ultimo item da list.
list = [1, 2, 3, 4 ,5]
print(list)
list[1] = 100
print(list[1])
print(list)
del list[3]
print(list)
#---------/--------/--------/--------/--------/
print(95 * '-')
#---------/--------/--------/--------/--------/
#                   APPEND
# novo_valor = 100
# list += [novo_valor]
# print(list)
list_append = [10,20,30,40]
print(list_append)
list_append.append(50)
list_append.append(60)
list_append.append(70)
print(list_append)
#---------/--------/--------/--------/--------/
print(95 * '-')
#---------/--------/--------/--------/--------/
#                   POP
#Nesses casos de lista pequena podemos apagar o valor final ou pelo valor no indice (.pop(3)) 3 = indice,tambem podemos armazenar esse valor em um variavel usando o pop.
list_pop = [10,20,30,40]
list_pop.append(50)
print(list_pop)
list_pop.pop()
print(list_pop)
#---------/--------/--------/--------/--------/
print(95 * '-')
#---------/--------/--------/--------/--------/
#                   CLEAR
list_clear = [10,20,30,40]
print(list_clear)
list_clear.clear()
print(list_clear)
#---------/--------/--------/--------/--------/
print(95 * '-')
#---------/--------/--------/--------/--------/
#                   INSERT
# A funcao .insert ela recebe dois valores: (0,5) primeiro valor que e o 0 significa que ele sera colocado no indice 0 que e o primerio lugar na list, ja o segundo valor que e o 5 sera o numero adicionado a list
list_insert = [10, 20, 30, 40]
print(list_insert)
list_insert.insert(0, 5)
print(list_insert)
#---------/--------/--------/--------/--------/
print(95 * '-')
#---------/--------/--------/--------/--------/
#                   EXTEND e +
# Metodo de concatenacao usando o sina de mais.
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
print(list_c)

#No caso de se usar o metodo .extend (list_d.extend(list_e)) voce esta chamando a lista e para extender na lista d se no caso de fizer isso jogando para outra lista esse valor sera NONE

list_d = [1, 2, 3]
list_e = [4, 5, 6]
#list_f = list_d.extend(list_e) -> valor none pos os valores vao se permanecer na list d
list_d.extend(list_e)
print(list_d)






