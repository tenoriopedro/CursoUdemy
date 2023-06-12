## @property - um getter no modo Pythonico
## getter - um metodo para obter um atributo
## cor -> get_color
## @property - é uma propriedade do objeto, ela
## é um metodo que se comporta como um atributo
## Geralmente é usada nas seguintes situações:
## - como getter
## para evitar quebrar codigo cliente
## para habilitar setter
## para executar ações ao obter um atributo
## Codigo cliente - é o codigo que usa seu codigo

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 123456

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)


#############################################



# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor
#
#     def get_cor(self):
#         return self.cor
#
# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())