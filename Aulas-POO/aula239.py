## CONTINUANDO AULA 236
## __new__ e __init__ em classes Python
## __new__ é o metodo responsavel por criar e
## retornar o novo objeto. Por isso, new recebe cls.
## __new__ DEVE retornar o objeto!!
## __init__ é o metodo responsavel por inicializar
## a instância. Por isso init recebe self.
## __init__ NÃO DEVE retornar nada (None)
## object é a sueper classe de uma classe

class A:
    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        return instancia


    def __init__(self, x):
        self.x = x
        print('Sou inutil')

    def __repr__(self):
        return 'A()'

a = A(123)
print(a.x)