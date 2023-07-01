palavra_secreta = 'agua'
tentativas = 3 + len(palavra_secreta)
letras_geradas = ''
acerto_tentativa = 0

while True:
    print(f'Total de tentavias: {tentativas}')
    letra = input('Digite uma letra: ').lower()
    acerto_tentativa += 1

    if tentativas < 0:
        print('Acabou suas tentativas')
        print('VOCÊ PERDEU')
        break

    if letra not in palavra_secreta:
        print('ERROU! Tente de novo..')
        tentativas -= 1
        continue
    if len(letra) > 1:
        print('Digite apenas uma letra..')
        continue
    if letra.isalpha() == False:
        print('ERRO!! Digite apenas letras..')
        continue

    if letra in palavra_secreta:
        print(f'Você acertou! Temos a letra "{letra.upper()}" na palavra secreta')
        letras_geradas += letra

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_geradas:
            palavra_formada += letra_secreta
            print(f'{letra_secreta}',end='')

        else:
            print('_',end='')
    print()
    if palavra_formada == palavra_secreta:
        print('PARABÉNS!!')
        print(f'VOCÊ CONSEGUIU, depois de {acerto_tentativa} tentativas')
        break

print('GAME OVER !!!')
