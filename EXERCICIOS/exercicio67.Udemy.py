operadores_validos = '+-*/'
n1 = 0
n2 = 0

while True:
    try:
        n1 = input('Digite um numero: ').replace(',', '.')
        n2 = input('Digite outro numero: ').replace(',', '.')
        if '.' in n1 or '.' in n2:
            n1 = float(n1)
            n2 = float(n2)
        else:
            n1 = int(n1)
            n2 = int(n2)
    except:
        print('ERRO!! Digitou algum numero errado, tente novamente...')
        continue
    print('Numeros corretos, vamos ao operador.')

    while True:
        operador = input('Digite o operador[+,-,*,/]: ')
        if operador not in operadores_validos:
            print('ERRO!! Você digitou um operador invalido.')
            continue
        if len(operador) > 1:
            print('ERRO!! Digite apenas um operador. ')
            continue
        else:
            break

    if operador == '+':
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif operador == '-':
        sub = n1 - n2
        print(f'{n1} - {n2} = {sub}')
    elif operador == '*':
        mult = n1 * n2
        print(f'{n1} * {n2} = {mult}')
    elif operador == '/':
        div = n1 / n2
        print(f'{n1} / {n2} = {div:.2f}')
    else:
        print('Você nao devia chegar aqui...')

    sair = input('Deseja sair [S/N]: ').strip().lower()[0]
    if sair == 's':
        break

print('FIM DO PROGRAMA')