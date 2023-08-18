while True:
    salario = input('Digite o salario: ')
    salario_float = float(salario)

    if salario_float <= 2000.00:
        print('Não paga imposto')

    elif salario_float >= 2000.01 and salario_float <= 3000.00:
        imposto_8_porcento = (salario_float* 0.08) 
        print(f'Deve pagar R$ {imposto_8_porcento:.2f} de imposto.')

    elif salario_float >= 3000.01 and salario_float <= 4500.00:
        imposto_18_porcento = (salario_float * 0.18) 
        print(f'Deve pagar R$ {imposto_18_porcento:.2f} de imposto.')

    else:
        imposto_28_porcento = (salario_float * 0.28)
        print(f'Deve pagar R${imposto_28_porcento:.2f} de imposto')
        
    sair = input('Quer sair? [s]air ').lower().startswith('s')
        
    if sair is True:
        break