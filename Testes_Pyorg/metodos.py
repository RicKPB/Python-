nome = input('Digite seu nome: ')

# O metodo .lower ele converte toda variavel str para minusculas mesmo e for escrita em maiscula
nome = nome.lower()

print(nome)

#--------////------------////-----------////-----------////

# O metodo .startswith ele serve para detectar se a variavel comeca com a letra determinada
nome = nome.lower().startswith('s')

#Ja o metodo .endswith ele serve para detectar se a variavel termina com a letra determinada
# nome = nome.lower().endswith()

# O metodo .upper deixa todas as letras da string em maiusculo.
frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum. '.upper()
    
print(frase)

# O metodo .count ele armazena a quantas vezes a palavra ou o numero apareceu no texto.

frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum. '
    
print(frase.count('Python'))
