'''
Introducao a desempacotamento 
'''

# Nesse caso de desempacotamento de list podemos ver que foi criado com uma variavel (nome1) e para o resto da list foi criado a variavel resto para poder armazenar o resto dos nomes da list (Nao e legal criar variaveis aonde se nao utilizara dentro do seu codigo, nesse caso voce coloca no nome da variavel como '_')
nome1, *_ = ['Gui', 'henrique', 'pig', 'felipe']
print(nome1)