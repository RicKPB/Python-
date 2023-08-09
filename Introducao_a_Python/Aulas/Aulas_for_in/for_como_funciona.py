"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
#Esse exemplo aonde usamos function e simplificado na hora que se usa o for como foi feito no exemplo abaixo, os dois sao a mesma coisa. 
texto = 'Python' #interavel
interador = iter(texto) #iterador

while True:
    try:
        letra = next(interador)
        print(letra)
    except StopIteration:
        break
    
print(95 * '-')
  
textos = 'Python'

for interadorr in textos:
    print(interadorr)