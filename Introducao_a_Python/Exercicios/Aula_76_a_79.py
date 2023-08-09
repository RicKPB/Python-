
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os 

palavra_secreta = 'computador'
letras_acertadas = ''
tentativas = 0

while True:
    
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Voce nao digitou uma letra')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas +=letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palvra formatada: ',palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('clear')
        
        print('Voce ganhou!! Parabens!!')
        print(f'A palavra secreta era {palavra_secreta}')
        print('Tentativas: ',tentativas)
        letras_acertadas = ''
        tentativas = 0
        