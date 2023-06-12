## Ainda sobre dataclass
## asdict e astuple em dataclasses
## Valores padrões, field e fields em dataclasses
from dataclasses import dataclass, asdict, astuple, field

@dataclass
class Pessoa:
    nome: str = field(default='MISSING')
    sobrenome: str = 'Not sent'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)

if __name__ == '__main__':
    p1 = Pessoa()
    print(p1)

    # print(asdict(p1).keys())
    # print(asdict(p1).values())
    # print(asdict(p1).items())
    # print(astuple(p1))
