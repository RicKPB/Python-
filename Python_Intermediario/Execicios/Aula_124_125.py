# Exercicio - sistema de perguntas e respostas

perguntas = [ 
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

acertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    print('Opções:')

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if 0 <= escolha_int < qtd_opcoes:
        # if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        print('Acertou!!')
        acertos += 1
    else: 
        print('Errou!')
    print()

print(f'acertou {acertos}')
print(f'de {len(perguntas)} perguntas')
