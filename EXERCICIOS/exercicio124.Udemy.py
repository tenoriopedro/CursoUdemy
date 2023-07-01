## Exercicio com sistema de perguntas e respostas

def linha():
    print('-'*30)

acertos = 0


perguntas =[
    {
        'Pergunta':'Quanto é 2+2?',
        'Opçoes':['2', '4', '6', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta':'Quanto é 5x5?',
        'Opçoes': ['15','20','25','30'],
        'Resposta': '25',
    },
    {
        'Pergunta':'Quanto é 10/2?',
        'Opçoes':['3','4','5','6'],
        'Resposta':'5',
    },
]

for pergunta in perguntas:
    ## Dividindo as perguntas
    print(f'- {pergunta["Pergunta"]}')

    ## Divindo as opções dentro das perguntas
    ## Colocando a resposta certa dentro de uma variavel (resposta_certa)
    resposta_certa = 0
    for k, opcao in enumerate(pergunta['Opçoes']):
        print(f'Opção {k + 1}) {opcao}')
        if opcao == pergunta['Resposta']:
            resposta_certa += k + 1

    ## Tratando da resposta do Usuário
    escolha = input('Escolha uma das opções: ')
    escolha = int(escolha)
    if escolha == resposta_certa:
        print('\033[32mAcertou!!!\033[m')
        acertos += 1
    else:
        print('\033[31mErrou!!!\033[m')

    linha()

## Mostra quantidade de acertos do Usuário
print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')