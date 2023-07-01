# Sets - Conjuntos em Python (tipo set)
#
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno

# Criando um set
# set(iterável) ou {1, 2, 3}

# s1 = set() # vazio
# s1 = {'Luiz', 1, 2, 3} # com dados

# Sets são eficientes para remover valores duplicados
# de iteraveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - Não tem indices;
# - Não garantem ordem;
# - São iteráveis (for, in, not in)

# s1 = { 1, 2, 3, 3, 3, 3, 3, 3, 1}
# print(s1)

# Metodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add('Luiz')
# s1.add(1)
# s1.update(('Ola mundo', 1, 2, 3, 4))
# s1.discard('Ola mundo')
# s1.discard('Luiz')
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença e simetrica ^ - Itens que não estão em ambos

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = s1 | s2
# s3 = s1 & s2
# s3 = s1 - s2
# s3 = s1 ^ s2
#
# print(s3)


## Exemplo de uso dos sets
letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Parabéns')
        break

    print(letras)
