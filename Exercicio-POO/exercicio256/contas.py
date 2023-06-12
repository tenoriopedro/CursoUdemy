from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo


    @abstractmethod
    def sacar(self, dinheiro):
        ...


    def depositar(self, dinheiro):
        self.saldo += dinheiro
        print(f'Deposito de {dinheiro:.2f} feito.\n'
              f'Seu saldo é de {self.saldo:.2f}')



class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.agencia},' \
               f'{self.conta},{self.saldo},{self.limite})'



    def sacar(self, dinheiro):
        conta_saldo = self.saldo - dinheiro
        limite_maximo = -self.limite

        if conta_saldo >= limite_maximo:
            self.saldo -= dinheiro
            print('Saque feito com sucesso.\n'
                  f'Você sacou {dinheiro:.2f} seu saldo é de {self.saldo:.2f}')
            return self.saldo

        print('SAQUE NEGADO.')
        print(f'Não foi possivel sacar a quantia de {dinheiro:.2f}')
        print(f'Seu saldo é de {self.saldo:.2f}')


class ContaPoupanca(Conta):
    def sacar(self, dinheiro):
        conta_saldo = self.saldo - dinheiro

        if conta_saldo >= 0:
            self.saldo -= dinheiro
            print('Saque feito com sucesso.\n'
                  f'Você sacou {dinheiro:.2f}')
            print(f'Seu saldo é de {self.saldo:.2f}')
            return self.saldo

        print('SAQUE NEGADO.')
        print(f'Não foi possivel sacar a quantia de {dinheiro:.2f}')
        print(f'Seu saldo é de {self.saldo:.2f}')

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.agencia},' \
               f'{self.conta},{self.saldo})'


if __name__ == '__main__':

    ...