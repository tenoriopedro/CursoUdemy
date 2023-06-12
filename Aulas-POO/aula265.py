## dataclasses - O que são dataclasses?
## O módulo dataclasses fornece um decorador e funções para criar métodos como
## __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
## usuários
## Em resumo: dataclasses são syntax sugar para criar classes normais.
## Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
## __init__ e __post_init__ em dataclasses
## configurações do decorator dataclass ( dataclass(...) )
## doc: https://docs.python.org/3/library/dataclasses.html


from dataclasses import dataclass

# @dataclass(init=False) ## decicidi que dataclass não tera init
# class Pessoa:          ## portando o __post_init__ não sera executado
#     nome: str
#     #idade: int
#     sobrenome: str

    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'
    #
    #
    #
    # def __post_init__(self):
    #     print('POS INIT')
        #self.nome_completo = f'{self.nome} {self.sobrenome}'


    # @property ## com getter
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'
    #
    # @nome_completo.setter ## com setter
    # def nome_completo(self, valor):
    #     nome, sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = sobrenome

@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str



if __name__ == '__main__':
    # p1 = Pessoa('Pedro', 'Tenório')
    # print(p1)
    # print(p1.nome_completo)
    lista = [Pessoa('A','Z'), Pessoa('B','Y'), Pessoa('C','X')]
    ordenadas = sorted(lista, reverse=False,
                       key=lambda p: p.nome)
    print(ordenadas)