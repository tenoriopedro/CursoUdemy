## Classes decoradoras (Decorator classes)

class Multiplicar:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado


@Multiplicar
def produto(x, y):
    return x * y

result = produto(2, 5)
print(result)