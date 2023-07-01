nome_usuario = str(input('Digite o seu primeiro nome: '))
if len(nome_usuario) <= 4:
    print('Seu nome é curto.')
if len(nome_usuario) == 6 or len(nome_usuario) == 5:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
print('Continuando...')
while True:
    idade_usuario = input(f'{nome_usuario}, qual a sua idade: ')
    if idade_usuario.isnumeric():
        idade_usuario = int(idade_usuario)
        if idade_usuario % 2 == 0:
            print('Sua idade é um numero par.')
            break
        else:
            print('Sua idade é um numero impar.')
            break
    else:
        print('ERRO!! Digite apenas numero inteiros.')

print('Ainda não vá embora..')
horario = input(f'{nome_usuario} que horas são: ')[:2]
print(f'{nome_usuario}', end=' ')
if horario.isnumeric():
    #print(horario)
    horas = int(horario)
if horas <= 23 and horas >= 18:
    print('esta de noite')
if horas <= 17 and horas >= 12:
    print('esta de tarde')
if horas <= 11 and horas >= 0:
    print('esta de manha')
print(f'HORA DE ASSISTIR WAKANDA')
