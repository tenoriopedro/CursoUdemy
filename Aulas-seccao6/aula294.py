





import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula294.csv'

lista_clientes = [
    {'nome': 'Pedro Tenório', 'endereço': 'Av 1, 22'},
    {'nome': 'Gabrielly Emidio', 'endereço': 'R. 2, "1"'},
    {'nome': 'Lucas Vasconcelos', 'endereço': 'Av. B, 3A'},
]

with open(CAMINHO_CSV, 'w', encoding='utf8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(arquivo,
                              fieldnames=nome_colunas
                              )
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)

# with open(CAMINHO_CSV, 'w', encoding='utf8') as arquivo:
#     nome_colunas = lista_clientes[0].keys()
#     escritor = csv.writer(arquivo)
#
#     escritor.writerow(nome_colunas)
#
#     for cliente in lista_clientes:
#         escritor.writerow(cliente.values())