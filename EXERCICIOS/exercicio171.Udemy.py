## somando listas

lista_1 = [1, 2, 3, 4, 5, 6, 7]
lista_2 = [1, 2, 3, 4,]
lista_soma = [
    x + y for x, y in zip(lista_1, lista_2)
]



# print(lista_1)
# print(lista_2)
# print(lista_soma)
lista_3 = []
for i in range(len(lista_2)):
    lista_3.append(lista_2[i] + lista_1[i])
print(lista_3)