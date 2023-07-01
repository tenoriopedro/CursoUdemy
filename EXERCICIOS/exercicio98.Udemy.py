## Exercicio 98 e 100
## Validando CPF(1ºdigito e 2ºdigito)
## Gerador de CPF
while True:

    try:
        cpf = input('Digite seu CPF: ').replace('.','').replace('-', '').strip()
        entrada_repetida = cpf == cpf[0] * len(cpf)
        if entrada_repetida:
            print('Digite um CPF valido')
            continue
        validar_1dgt = cpf[:-2]
        validar_2dgt = cpf[:-1]

        ## PRIMEIRO DIGITO
        soma_1dgt = 0
        mult_1dgt = 10

        for numero in validar_1dgt:
            numero = int(numero)
            multiplicar = mult_1dgt * numero
            #print(f'{mult} x {numero} = {multiplicar}')
            mult_1dgt -= 1
            soma_1dgt += multiplicar


        resultado_final_1dgt = (soma_1dgt * 10) % 11

        ## SEGUNDO DIGITO

        soma_2dgt = 0
        mult_2dgt = 11

        for numero in validar_2dgt:
            numero = int(numero)
            multiplicar = mult_2dgt * numero
            mult_2dgt -= 1
            soma_2dgt += multiplicar

        resultado_final_2dgt = (soma_2dgt * 10) % 11

        ##VERICANDO OS RESULTADOS

        if resultado_final_1dgt > 9:
            valor_1dgt = 0
        else:
            valor_1dgt = resultado_final_1dgt

        if resultado_final_2dgt > 9:
            valor_2dgt = 0
        else:
            valor_2dgt = resultado_final_2dgt

        ##VALIDAÇÃO DO CPF

    except (ValueError, IndexError):
        print('Digite um CPF valido.')
        continue

    else:
        valor_1dgt = str(valor_1dgt)
        valor_2dgt = str(valor_2dgt)
        validação = valor_1dgt + valor_2dgt
        if cpf[-2:] == validação:
            print('CPF VALIDO')
            break
        else:
            print('CPF INVALIDO')