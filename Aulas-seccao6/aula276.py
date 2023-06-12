## datetime.timedelta e dateutil.relativetimedelta (calculando datas)


from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/04/2023 20:11:15', fmt)
delta = relativedelta(data_fim, data_inicio)
# print(data_fim + relativedelta(seconds=60))

print(delta)
# delta = timedelta(days=10)
# print(data_fim + delta)

# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
