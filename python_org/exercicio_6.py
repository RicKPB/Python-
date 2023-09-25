#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def coercaoHoras(*agrs):

    while True:
        
        hora = int(input('Digite a hora: '))
        minutos = int(input('Digite os minutos: '))
        
        if hora < 24 and minutos < 60:
            if hora >= 13:
                horario_A_M = hora - 12

                print(f'{horario_A_M}:{minutos}')
        
            else:
                print(f'{hora}:{minutos}')
        
        else:
            print('O horario digitado nao e real tente novamente')
            continue
        #---------------SAIR SISTEMA------------------
        sair = input('Deseja [S]air: ').upper().startswith('S')

        if sair is True:
            print('Sistema finalizado')
            break

coercaoHoras()