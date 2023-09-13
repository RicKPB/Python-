"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'luis otavio'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
#Metodo aonde podemos editar uma str imutavel
print(string.capitalize())
#metodo aonde executa o nome como a primeira letra maiuscula e o restante minuscula 


number = '10'

print(number.zfill(15))
#Quantidade de numero que vao aparecer no caso vao aparecer 13 0 antes e depois o numero da variavel que e 10.

