nome = input('Digite seu nome: ')
letras = nome.split()
c = 0
novo_nome = ''
while c < len(nome):
    letra = nome[c]
    novo_nome += f'*{letra}'

    c += 1

print(novo_nome, end='*')
