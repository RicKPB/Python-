# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

from random import randint

def gamesCraps(*args):

    while True:
        dado = (randint(2,12))
        print(dado, end='\n')

        if dado == 7 and dado == 11:
            print('Voce e Natural.')
            print('Voce ganhou!!!')
            break
        
        elif dado == 2 and dado == 3 and dado == 12:
            print('Voce e um craps.')
            print('Voce perdeu!!')
            break

        elif dado >= 4 and dado <= 10: 
            print('Voce tirou o ponto, gire novamente.')
        
        

gamesCraps()
