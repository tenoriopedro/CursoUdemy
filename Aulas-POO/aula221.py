## super() é a super classe na sub classe
## Classe principal (Pessoa)
##   -> super class, base class, parent class
## Classes filhas (Cliente)
##   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super().upper()
#         print('DEPOIS')
#         return retorno
#
#
# string = MinhaString('Pedro')
# print(string.upper())


class A(object):
    atributo_a = 'valor a'

    def __init__(self, qualquer, outra_coisa):
        self.qualquer = qualquer
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        print('Com licença')
        super().__init__(*args, **kwargs)


    def metodo(self):
        # super().metodo() # B
        # super(B, self).metodo() # A
        # super(A, self).metodo() # object
        # A.metodo(self)
        # B.metodo(self)
        print('C')

# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('Atributo',' kk')
print(c.qualquer)
print(c.outra_coisa)

# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()
