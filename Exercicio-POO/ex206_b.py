import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


with open('salvando.json', 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)
    p1 = Pessoa(**dados)
    print(p1.nome, p1.idade)