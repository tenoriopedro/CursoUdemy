## Composição é uma especialização da agregação.
## Mas nela, quando o objeto "pai" for apagado, todas
## as referencias dos objetos filhos também são apagadas

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua,numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO', self.rua, self.numero)

cliente1 = Cliente('Pedro')
cliente1.inserir_enderecos('Av.Brasil', 54)
cliente1.inserir_enderecos('Rua B', 6745)
# print(cliente1.enderecos[0].rua)
# print(cliente1.enderecos[1].rua)
cliente1.listar_enderecos()


print('>>>>> FIM DO CODIGO')