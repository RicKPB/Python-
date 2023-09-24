def somaNums(*args):
    lista = ([])
    i = 0
    while True:

        if i < 3:
            valor = float(input('Digite um valor valido: '))
            lista.append(valor)
            print(lista)

        else:
            break
        i += i



somaNums()