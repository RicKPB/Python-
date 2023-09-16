"""
    Exercicios
    Criar funcoes que duplicam, triplicam e quadruplicam
    o numero rebido pelo parametro
"""

valor = float(input('Digite um valor: '))


def multiplicadores(*args):
    
    while True:
        global valor
        selectMult = input('Voce deseja [M]ultiplicar, [T]riplicar ou [Q]uadruplicar: ' ).upper()
        
        if 'M' in selectMult:
            
            duplicador = valor * 2
            print(f'{valor=} * 2 = {duplicador:.2f}')
        
        elif 'T' in selectMult:
            triplicador = valor * 3
            print(f'{valor=} * 3 = {triplicador:.2f}') 

        elif 'Q' in selectMult:
            quadruplicador = valor * 4
            print(f'{valor=} * 4 = {quadruplicador:.2f}') 

        else:
            print('Letra digitada esta incorreta!! <%&%SystemERROR%&%>')
            break 

multiplicadores()

#-------//-------//---------//--------//--------
print('-' * 95)
#-------//-------//---------//--------//--------


"""
    Correcao do Luiz Otavio
"""

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicador = criar_multiplicador(2)
print(duplicador(2))
triplicador = criar_multiplicador(3)
print(triplicador(2))
quadruplicador = criar_multiplicador(4)
print(quadruplicador(2))

