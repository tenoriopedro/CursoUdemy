from contas import ContaCorrente, ContaPoupanca

class Pessoa:
    def __init__(self,nome, idade):
        self.nome_cliente = nome
        self.idade_cliente = idade


    @property
    def nome(self):
        return self.nome_cliente

    @nome.setter
    def nome(self, nome):
        self.nome_cliente

    @property
    def idade(self):
        return self.idade_cliente

    @idade.setter
    def idade(self, idade):
        self.idade_cliente


class Cliente(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome,idade)
        self.conta: contas.Conta | None = None

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.nome}, {self.idade})'


if __name__ == '__main__':


    c1 = Cliente('Pedro', 28)
    c1_conta_poupanca = ContaPoupanca(111,222,0)
    c1_conta_corrente = ContaCorrente(111,2222,0,0)
    print(c1)
    print(c1_conta_poupanca)
    print(c1_conta_corrente)
