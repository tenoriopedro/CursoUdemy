## Escopo da classe e de metodos da classe

class Animal:

    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return f'{self.nome} esta comendo {alimento}'

leao = Animal('Leão')
print(leao.nome)
print(leao.comendo('carne'))