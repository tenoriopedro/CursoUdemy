## Criar funções que duplicam, triplicam, quadruplicam o numero recebido
## como parametro

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)
quadruplo = criar_multiplicador(4)

numero = input('Digite um numero: ')
numero = int(numero)
print(f'dobro: {dobro(numero)}\n'
     f'triplo: {triplo(numero)}\n'
      f'quadruplo: {quadruplo(numero)}')

