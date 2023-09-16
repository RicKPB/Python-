'''
Clousure e funçōes que retornam outras funçōes. 
'''


def criar_saudacao(saudacao):
    def saudar(nome):
        return (f'{saudacao} {nome}')
    return saudar


nome_saudacao = str(input('Digite seu nome: '))

bom_dia = criar_saudacao('Bom dia')
print(bom_dia(nome_saudacao))
boa_tarde = criar_saudacao('Boa tarde')
print(boa_tarde(nome_saudacao))
boa_noite = criar_saudacao('Boa noite')
print(boa_noite(nome_saudacao))

#---------------------------------------------------
print