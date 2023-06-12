import contas
import pessoa

class Banco:
    def __init__(self,
                 agencias: list[int] | None = None,
                 contas: list[contas.Conta] | None = None,
                 clientes: list[pessoa.Pessoa] | None = None):

        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False


    def checa_cliente(self,cliente):
        if cliente in self.clientes:
            return True
        return False


    def checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def checa_conta_cliente(self,cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: pessoa.Pessoa, conta: contas.Conta):
        return self.checa_agencia(conta) and \
            self.checa_cliente(cliente) and  \
            self.checa_conta(conta) and \
            self.checa_conta_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.agencias!r}), ' \
               f'({self.contas!r}), ({self.clientes!r})'

if __name__ == '__main__':

    c1 = pessoa.Cliente('Pedro', 28)
    conta_corrente_c1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = conta_corrente_c1

    c2 = pessoa.Cliente('Gabrielly', 30)
    conta_poupanca_c2 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = conta_poupanca_c2

    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([c1.conta, c2.conta])
    banco.agencias.extend([111, 222])
    print(banco)

    if banco.autenticar(c1, c1.conta):
        c1.conta.depositar(20)
        print(c1.conta)