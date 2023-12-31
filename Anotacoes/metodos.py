nome = input('Digite seu nome: ')

# O metodo .lower ele converte toda variavel str para minusculas mesmo e for escrita em maiscula
nome = nome.lower()

print(nome)

#---------/--------/--------/--------/--------/
print('-' * 95)
#---------/--------/--------/--------/--------/

# O metodo .startswith ele serve para detectar se a variavel comeca com a letra determinada
nome = nome.lower().startswith('s')

#Ja o metodo .endswith ele serve para detectar se a variavel termina com a letra determinada
# nome = nome.lower().endswith()

#---------/--------/--------/--------/--------/
print('-' * 95)
#---------/--------/--------/--------/--------/

# O metodo .upper deixa todas as letras da string em maiusculo.
frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum. '.upper()
    
print(frase)

#---------/--------/--------/--------/--------/
print('-' * 95)
#---------/--------/--------/--------/--------/

# O metodo .count ele armazena a quantas vezes a palavra ou o numero apareceu no texto.

frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum. '
    
print(frase.count('Python'))

#---------/--------/--------/--------/--------/
print('-' * 95)
#---------/--------/--------/--------/--------/

# O metodo .append serve para voce adicionar um numero no final de uma lista

list = [10,20,30,40]

list.append(50)
print(list)

#---------/--------/--------/--------/--------/
print('-' * 95)
#---------/--------/--------/--------/--------/

# O metodo .pop serve para elminiar o ultimo elemento da lista
list = [10,20,30]
list.append(50)
list.pop()
list.pop(2) #remover sobre o indice

#---------/--------/--------/--------/--------/
print('-' * 95)
#---------/--------/--------/--------/--------/

# O metodo .strip() serve para apagra os espacos do comeco e do fim da frase.

frase = '  Hello World  '
print(frase.strip())
# Em casos especificos tambem temos o rstrip(espaco a direita) e o lstrip(espaco a esquerda)
