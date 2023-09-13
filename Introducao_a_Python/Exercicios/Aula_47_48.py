"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""


nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

nome_str = str(nome)
idade_int = int(idade)


if (nome_str!= '') and (idade_int != 0):
    print(f'Seu nome é {nome_str}')
    print(f'Seu nome invertido é {nome_str[::-1]}')

    if ' ' in nome_str:
        print(f'Seu nome contem espaços')
    else:
        print(f'Seu nome não cotem espaços')
        
    print(f'Seu nome tem {len(nome_str)} de letras')
    print(f'A primeira letra do seu nome é {nome_str[0]}')
    print(f'A ultima letra do seu nome é {nome_str[-1]}')
    
else:
    print("Desculpe, você deixou campos vazios.")