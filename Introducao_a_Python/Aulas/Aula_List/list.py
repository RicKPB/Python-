'''
Lista em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo,
Conhecimentos reutilizaveis -indices e fatiamentos.
Metodos uteis -> append, insert, pop, del, clear, extend, +
'''

#.....+12345
#.....-54321
str = 'ABCDE' #5 CARACTERES(len)

#---------/--------/--------/--------/--------/
#list = list('Henrique', 'Jao', 'Gordao', 'Lsete')
#.......0............1......2.........3.....
#.......-4.........-3......-2........-1.....
list = ['Henrique', 'Jao', 'Gordao', 'Lsete'] #Melhor de ser feito!
print(type(list))
print(list)
print(list[2])
print(list[1], type(list[1]))
#---------/--------/--------/--------/--------/
print(95 * '-')
#---------/--------/--------/--------/--------/
vazio = []
print(bool(vazio))#False
#---------/--------/--------/--------/--------/
print(95 * '-')
#---------/--------/--------/--------/--------/
list_tipos = [123, False,'Henrique',10.2]
print(list_tipos)
#---------/--------/--------/--------/--------/
print(95 * '-')
#---------/--------/--------/--------/--------/
list_alterado = [32, 'Joao', 1900.82]
list_alterado[-3] = 10
print(list_alterado[0], type(list_alterado[0]))

