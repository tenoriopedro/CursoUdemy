## Funções decoradoras e decoradores com classes

def adiciona_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls


def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args,**kwargs)

        if 'Terra' in resultado:
            return f'Você esta em casa, Terra'
        return resultado
    return interno

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O planeta {self.nome}'


vasco = Time('Vasco')
flamengo = Time('Flamengo')
terra = Planeta('Terra')
marte = Planeta('Marte')

print(vasco)
print(flamengo)
print(terra)
print(marte)
print(terra.falar_nome())
print(marte.falar_nome())