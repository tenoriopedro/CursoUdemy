## Polimorfismo em Python Orientado a Objetos
## Polimorfismo é o princípio que permite que
## classes derivadas de uma mesma superclasse
## tenham métodos iguais (com mesma assinatura)
## mas comportamentos diferentes.
## Assinatura do método = Mesmo nome e quantidade
## de parâmetros (retorno não faz parte da assinatura)
## Opinião + princípios que contam:
## Assinatura do método: nome, parâmetros e retorno iguais
## SO"L"ID
## Princípio da substituição do liskov
## Objetos de uma superclasse devem ser substituiveis
## por objetos de uma subclasse sem quebrar a aplicação
## Sobrecarga de métodos (overload) (Python NO)
## Sobreposição de métodos (override) (Python YES)
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):

    def enviar(self) -> bool:
        print('Email: enviando - ', self.mensagem)
        return True
class NotificacaoSMS(Notificacao):

    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação Enviada')
    else:
        print('Notificação NAO Enviada')

notificacao_email = NotificacaoEmail('Testando email')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Testando SMS')
notificar(notificacao_sms)