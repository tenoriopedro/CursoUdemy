## METODO DE CLASSE + FACTORIES
## SÃO METODOS ONDE "self" SERÁ "cls" , OU SEJA,
## AO INVER DE RECEBER A INSTÂNCIA NO PRIMEIRO
## PARÂMETRO, RECEBERMOS A PROPRIA CLASSE


class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

p1 = Pessoa('Joao', 34)
p2 = Pessoa.criar_com_50anos('Pedro')
p3 = Pessoa.criar_sem_nome(25)
# print(Pessoa.ano)
# p1.metodo_de_classe()
print(p3.nome, p3.idade)
print(p2.nome, p2.idade)