from abc import ABC, abstractmethod

class Conta(ABC):

    @abstractmethod
    def _sacar(self, dinheiro):...


    def saque_sucess(self, conta_):
        return self._sacar(f'Saque feito com sucesso.')

    def saque_erro(self, conta_):
        return self._sacar(f'Erro ao fazer o saque.')


    @abstractmethod
    def _depositar(self, dinheiro):...


    def depositar_sucess(self, conta):
        return self._depositar(f'Deposito feito com sucesso.')

    def depositar_erro(self, conta):
        return self._depositar('Erro ao fazer o deposito.')

class ContaCorrente(Conta):
    def sacar(self, dinheiro):...

    def depositar(self, dinheiro):
        ...

class ContaPoupança(Conta):
    def sacar(self, dinheiro):...

    def depositar(self, dinheiro):
        ...