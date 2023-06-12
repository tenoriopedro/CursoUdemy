## Encapsulamento (modificadores de acesso: public, protected, privated
## Python NÃO TEM modificadores de acesso
## Mas podemos seguir as seguintes convenções
##  (sem underline) = public
##          pode ser usado em qualquer lugar
## _ (um undeline = protected
##          não DEVE ser usado fora da classe
##          ou suas subclasses.
## __ (dois underlines = private
##        "name mangling" (desfiguração de nomes) em Python
##         so DEVE ser usado na classe em que foi declarado.


class Foo:
    def __init__(self):
        ...