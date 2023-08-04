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
list = [1, 2, 3, 4]
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
#Nesses casos de lista pequena podemos apagar ou adicionar pelo valor no indice (.pop(3)) 3 = indice
list_pop = [10,20,30,40]
list_pop.append(50)
print(list_pop)
list_pop.pop()
print(list_pop)




