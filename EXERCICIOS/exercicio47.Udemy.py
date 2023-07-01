try:
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
except(ValueError, TypeError):
    print('Você deixou o campo da idade vazio.')
else:

    if '' == nome:
        print('Você não digitou seu nome.')
    else:
        print(f'Seu nome é {nome}')
        nome_invertido = ' '
        for c in range(len(nome) -1, -1, -1):
            nome_invertido += nome[c]

        print(f'O inverso de {nome} é {nome_invertido.lower()}') # ou usar {nome[::-1]} (para nome invertido)
        nome = nome.replace(' ', '')
        print(f'Seu nome tem {len(nome)} letras')
        print(f'Primeira letra do seu nome é {nome[0]}')
        print(f'A ultima letra do seu nome é {nome[-1]}')