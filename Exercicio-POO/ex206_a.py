import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Pedro', 28)
print(p1.nome, p1.idade)

dict = p1.__dict__
print(dict)

with open('salvando.json', 'w', encoding='utf8') as arquivo:
    json.dump(dict, arquivo, indent=2, ensure_ascii=False)