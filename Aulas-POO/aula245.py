## Metodo especial __call__
## callable é algo que pode ser executado com parenteses
## Em classes normais, __call__ faz a instancia de uma
## classe "callable"


class CallMe:
    def __init__(self,phone):
        self.phone = phone

    def __call__(self,*args,**kwargs):
        print('Chamando', self.phone)


call_1 = CallMe('123456')
call_1()