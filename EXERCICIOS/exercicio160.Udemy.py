# 1º Exercicio: Aumentar os preços dos produtos em 10%
# 2º Exercicio: Ordene os nomes dos produtos por ordem decrescente
# 3º Exercicio: Ordene os preço dos produtos por ordem crescente
# Faça um deep copy em todos exercicios

import copy


def exibir(lista):
    for item in lista:
        print(item)
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


## EXERCICIO 1:
print('Produtos Original')
print(*produtos, sep='\n')

novos_produtos = copy.deepcopy(produtos)

for i in novos_produtos:
    valor = i['preco']
    i['preco'] = f'{valor + (valor * 10 / 100):.2f}'
print('-' *30)
print('Produtos com aumento de 10%.')
for n in novos_produtos:
    print(n)


## EXERCICIO 2:
print('-' *30)
print('Produtos ordenado por nome.')
produtos_ordenado_por_nome = copy.deepcopy(produtos)
produtos_ordenado_por_nome = sorted(produtos, key=lambda item: item['nome'], reverse=True)
exibir(produtos_ordenado_por_nome)


## EXERCICIO 3:
print('-'*30)
print('Produtos ordenado por preco.')
produtos_ordenado_por_preco = copy.deepcopy(produtos)
produtos_ordenado_por_preco = sorted(produtos, key=lambda item: item['preco'])
exibir(produtos_ordenado_por_preco)