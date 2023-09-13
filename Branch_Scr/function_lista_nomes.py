'''
Teste para adicionar nomes em listas diferentes direto de function
'''

def nome(*args):
    lista_nomes_curto = []
    lista_nomes_medio = []
    lista_nomes_longo = []
    lista_nomes = []
    
    for i in range(10):
        nome = input('Digite seu nome: ')
        lista_nomes.append(nome)
     
        if len(nome) <= 4:
            lista_nomes_curto.append(nome)
        elif len(nome) > 4 and len(nome) <= 7:
            lista_nomes_medio.append(nome)
        else:
            lista_nomes_longo.append(nome)
       
    print(lista_nomes)
    print(lista_nomes_longo) 
    print(lista_nomes_medio)
    print(lista_nomes_curto)


nome()