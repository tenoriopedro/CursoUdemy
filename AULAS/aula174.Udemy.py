# Combinations, Permutations e Product - itertools
# Combinations -> Ordem não importa - iteravel + tamanho do grupo
# Permutations -> Ordem importa
# Produto -> Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia'
]
camisetas = [
    ['preta', 'branca'],
    ['P','M','G'],
    ['masculino', 'feminino'],
    ['algodão', 'poliester']
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))