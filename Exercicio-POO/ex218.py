# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça ligação entre Carro tem Motor
# OBS.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante
# OBS.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Motor:
    def __init__(self, nome):
        self.nome = nome
        self.auto = []

    def adicionar_carro(self, *carros):
        for carro in carros:
            self.auto.append(carro)

    def mostrar_carros(self, nome_fabricante):
        marca = Fabricante(nome_fabricante)
        for carro in self.auto:
            print(f'{carro.nome} {marca.nome} {self.nome}')

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

class Carro:
    def __init__(self, nome):
        self.nome = nome


motor = Motor('1.5')
carro_1, carro_2, carro_3 = Carro('Punto'), Carro('Palio'), Carro('Stilo')
motor.adicionar_carro(carro_1, carro_2, carro_3)
motor.mostrar_carros('Fiat')

motor = Motor('1.0')
carro_1, carro_2, carro_3 = Carro('Megane'), Carro('Clio'), Carro('Laguna')
motor.adicionar_carro(carro_1, carro_2, carro_3)
motor.mostrar_carros('Renault')


#############################################

## OUTRA MANEIRA

# class Carro:
#     def __init__(self, nome):
#         self.nome = nome
#         self._motor = None
#         self._fabricante = None
#
#     @property
#     def motor(self):
#         return self._motor
#
#     @motor.setter
#     def motor(self, valor):
#         self._motor = valor
#
#     @property
#     def fabricante(self):
#         return self._fabricante
#
#     @fabricante.setter
#     def fabricante(self, valor):
#         self._fabricante = valor
#
#
# class Motor:
#     def __init__(self, nome):
#         self.nome = nome
#
#
# class Fabricante:
#     def __init__(self, nome):
#         self.nome = nome