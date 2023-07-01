## Trabalhando com JSON

import json

# pessoa = {
#   "nome": "Pedro",
#   "sobrenome": "Tenório",
#   "enderecos": [
#     {"rua": "R1","numero": 32},
#     {"rua": "R2","numero": 55}
#   ],
#   "altura": 1.8,
#   "numeros_preferidos": (2,4,6,8,10),
#   "dev": True,
#   "nada": None
# }

with open('aula190.Udemy.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    #print(pessoa)
    #print(pessoa['enderecos'][0]['rua'])