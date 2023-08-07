#Mesmo excicio da aula 76 ate a 79 so que feio sem ver as aulas e o codigo.


import os

palavra_secreta = 'Maconha'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1
    
    if len(letra_digitada) < 1:
        print('Digite somente uma palavra')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formatada = ''
    for letras_secreta in palavra_secreta:
        if letras_secreta in letras_acertadas:
            palavra_formatada += letras_secreta
        else:
            palavra_formatada += '*'
    
    print('Palvra formatada: ',palavra_formatada)
    
    if palavra_formatada == palavra_secreta:
        os.system('clear')
        
        print('Voce ganhou!! Parabens!!')
        print(f'A palavra secreta era {palavra_secreta}')
        print('Tentativas: ',tentativas)
        letras_acertadas = ''
        tentativas = 0
  