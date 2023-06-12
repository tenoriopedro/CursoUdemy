# string.Template para substituir variáveis em textos
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template

import locale
from datetime import datetime
import string
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula298.txt'
locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float ) -> str:
    brl = 'R$' + locale.currency(numero, symbol=False, grouping=True)
    return brl

data = datetime(2023, 4, 18)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_567),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone= '+55 (11) 7890-5432'
)


with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()

    template = string.Template(texto)
    print(template.substitute(dados))