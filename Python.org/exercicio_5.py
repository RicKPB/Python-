#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaimposto(*args):

    taxa_imposto = int(input('Digite o valor do imposto: '))
    custo_produto = float(input('Digite o valor do podruto: '))
    return (0.01*taxa_imposto)*custo_produto + custo_produto

soma=somaimposto(10, 1000)
print(soma)