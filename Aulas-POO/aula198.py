## INTRODUÇÃO A CLASSES


# string = 'Pedro' # str
# print(string.upper())

## ATRIBUTOS

# class Pessoa:
#     def __init__(self, nome, sobrenome):
#         self.nome = nome
#         self.sobrenome = sobrenome
#
#
# p1 = Pessoa('Pedro', 'Tenório')
# # p1.nome = 'Pedro'
# # p1.sobrenome = 'Tenorio'
# print(p1.nome, p1.sobrenome)
# print(p1.sobrenome)

## METODOS

class Carro:
    def __init__(self, nome='sem nome'):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()