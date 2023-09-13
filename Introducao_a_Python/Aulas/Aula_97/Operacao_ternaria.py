'''
Operacao ternaria -> Condicional de uma linha
<valor> if <condicao> else <outro valor>
'''

#--------//-------------//-----------------//

print('Valor' if True else 'Outro valor')
print('Valor' if False else 'Outro valor')
#--------//-------------//-----------------//
print('-'* 95)
#--------//-------------//-----------------//

condicao = 10==10
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)
#--------//-------------//-----------------//
print('-'* 95)
#--------//-------------//-----------------//

# Parte execicio CPF

digito = 10
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)
#--------//-------------//-----------------//
print('-'* 95)
#--------//-------------//-----------------//

print('valor' if False else 'Outro valor' if False else 'Fim')