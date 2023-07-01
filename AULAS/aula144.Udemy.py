# dir, hasattr e getattr em Python

string = 'Pedro'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe', metodo)
    print(getattr(string, metodo)())
else:
    print('Não existe o metodo', metodo)
