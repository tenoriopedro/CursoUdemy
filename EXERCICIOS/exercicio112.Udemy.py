## Exercícios com funções

## Multiplicar todos argumentos não nomeados recebidos


def mult(*args):
    produto = 1
    for numero in args:
        produto *= numero

    return produto

valor = mult(1,2,9,5,6)
print(valor)


## Numero par ou impar

def parImpar(numero):
    if numero % 2 == 0:
        ## retorna par
        return f'{numero} é um numero par'
    ## retorna impar
    return f'{numero} é um numero impar'

num = parImpar(2)
print(num)