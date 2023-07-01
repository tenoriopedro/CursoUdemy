## GERADOR DE CPFs

from random import randint
from modulo_ex98 import validador


print('~' *30)
print('GERADOR DE CPF'. center(30))
print('~' *30)


numero_do_estado = validador.verificaEstado('Digite o seu Estado: ')

print(numero_do_estado)
numeros_gerados = ''
for c in range(0, 8):
     numero = randint(0, 9)
     numero = str(numero)
     numeros_gerados += numero

numeros_gerados += numero_do_estado

#print(numeros_gerados)
#
validar_1dgt = numeros_gerados
#validar_2dgt = cpf[:-1]

##GERAR PRIMEIRO DIGITO
soma_1dgt = 0
mult_1dgt = 10

for numero in validar_1dgt:
    numero = int(numero)
    multiplicar = mult_1dgt * numero
    # print(f'{mult} x {numero} = {multiplicar}')
    mult_1dgt -= 1
    soma_1dgt += multiplicar

resultado_final_1dgt = (soma_1dgt * 10) % 11

## GERAR SEGUNDO DIGITO
resultado_final_1dgt = str(resultado_final_1dgt)
validar_2dgt = numeros_gerados + resultado_final_1dgt
soma_2dgt = 0
mult_2dgt = 11

for numero in validar_2dgt:
    numero = int(numero)
    multiplicar = mult_2dgt * numero
    mult_2dgt -= 1
    soma_2dgt += multiplicar

resultado_final_2dgt = (soma_2dgt * 10) % 11

##VERICANDO OS RESULTADOS
resultado_final_1dgt = int(resultado_final_1dgt)
resultado_final_2dgt = int(resultado_final_2dgt)
if resultado_final_1dgt > 9:
    valor_1dgt = 0
else:
    valor_1dgt = resultado_final_1dgt

if resultado_final_2dgt > 9:
    valor_2dgt = 0
else:
    valor_2dgt = resultado_final_2dgt

print(f'CPF gerado: {numeros_gerados}-{resultado_final_1dgt}{resultado_final_2dgt}')
