## Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager
@contextmanager
def my_open(caminh_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminh_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as error:
        print('Ocorreu um erro', error)
    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open('aula242.txt', 'w') as arquivo:
    arquivo.write('Oi',123)
    print('OPEN', arquivo)