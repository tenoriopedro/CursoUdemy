## CONTINUAÇÃO AULA212
## ATRIBUTOS QUE COMEÇAM COM UM OU DOIS UNDERLINES(_)
## NÃO DEVEM SER USADOS FORA DA CLASSE
class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'preta'
# getter = obter valor
print(caneta.cor)
print(caneta.cor_tampa)
