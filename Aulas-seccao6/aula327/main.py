# PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# for page in reader.pages:
#     print(page)

# page1 = reader.pages[0]
# print(page1.extract_text())
# print(page1.images)
# image1 = page1.images[0]

# with open(PASTA_NOVA / image1.name, 'wb') as fp:
#     fp.write(image1.data)

## Para paginas dentro de um arquivo só
# writer = PdfWriter()
#
#
# with open(PASTA_NOVA / 'NOVO_PDF.pdf', 'wb') as fp:
#     for page in reader.pages:
#         writer.add_page(page)
#
#     writer.write(fp)

## Para paginas em arquivos separados

# for i, page in enumerate(reader.pages):
#     writer = PdfWriter()
#     with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as fb:
#         writer.add_page(page)
#         writer.write(fb)

files = [
    PASTA_NOVA / 'page0.pdf',
    PASTA_NOVA / 'page1.pdf'
]
merger = PdfMerger()
for file in files:
    merger.append(file)


with open(PASTA_NOVA / 'merged.pdf', 'wb') as fb:
    merger.write(fb)

