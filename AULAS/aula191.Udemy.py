# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None): ## se não passar nenhum parametro
    if lista is None:
        lista = []          ## Cria-se uma nova lista independente
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Viviane', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)

## Nenhuma lista afeta a outra