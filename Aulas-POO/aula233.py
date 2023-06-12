## Criando Exceptions em Python Orientado a Objetos
## Para criar uma Exception em Python, você só
## precisa herdar de alguma exceçãp de linguagem.
## A recomendação da DOC é herdar de Exception.
## https://docs.python.org/3/library/exceptions.html
## Criando exceções (comum colocar Error ao final)
## Levantando (raise) // Lançando (throw) exceções
## Relançando exceções
## Adicionando notas em exceções (3.11.0)
class MyError(Exception):
        ...
class OtherError(Exception):
    ...

def levantar():
    exception_ = MyError('a', 'b', 'c')
    raise exception_

try:
    levantar()
except (MyError) as error:
    print(error.__class__.__name__)
    print(error.args)
    