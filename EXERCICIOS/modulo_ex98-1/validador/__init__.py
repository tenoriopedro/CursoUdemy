estados =['RS', 'DF', 'GO', 'MT', 'MS', 'TO',
          'AM', 'PA', 'RR', 'AP', 'AC', 'RO',
          'CE', 'MA', 'PI', 'PB', 'PE', 'AL',
          'RN', 'BA', 'SE', 'MG', 'RJ', 'ES',
          'SP', 'PR', 'SC']

def verificaEstado(msg):
    while True:
        estado = input(msg).upper()
        if len(estado) > 2:
            print('ERRO! Digite de acordo com o exemplo.')
            continue
        elif estado.isalpha() == False:
            print('ERRO! Digite de acordo com o exemplo.')
            continue
        elif estado not in estado:
            print('Estado incorreto.')
            continue
        else:
            break

    numero_1 = 'DF', 'GO', 'MG', 'MS', 'TO'
    numero_2 = 'AM', 'PA', 'RR', 'AP', 'AC', 'RO'
    numero_3 = 'CE', 'MA', 'PI'
    numero_4 = 'PB', 'PE', 'AL', 'RN'
    numero_5 = 'BA', 'SE'
    numero_6 = 'MG'
    numero_7 = 'RJ', 'ES'
    numero_8 = 'SP'
    numero_9 = 'PR', 'SC'
    numero_0 = 'RS'

    numero_estado = ''
    if estado in numero_0:
         numero_estado = '0'
    elif estado in numero_1:
          numero_estado = '1'
    elif estado in numero_2:
        numero_estado = '2'
    elif estado in numero_3:
        numero_estado = '3'
    elif estado in numero_4:
        numero_estado = '4'
    elif estado in numero_5:
        numero_estado = '5'
    elif estado in numero_6:
        numero_estado = '6'
    elif estado in numero_7:
        numero_estado = '7'
    elif estado in numero_8:
        numero_estado = '8'
    elif estado in numero_9:
        numero_estado = '9'

    return numero_estado