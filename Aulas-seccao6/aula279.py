## Usando calendar para calendários e datas
## https://docs.python.org/3/library/calendar.html
## calendar é usado para coisas genéricas de calendarios e datas.
## Com calendar, você pode saber coisas como:
## - Qual o ultimo dia do mês (ex:monthrange)
## - Qual o nome e numero do dia de determinada data (ex: weekday)
## - Criar um calendario em si (ex: monthcalendar)
## - Trabalhar com coisas especificas de calendarios (ex: calendar, month)
## Por padrão dia da semana começa com 0 até 6
## 0 = segunda-feira | 6 = domingo

import calendar

# print(calendar.calendar(2023))
# print(calendar.month(2023, 4))

# primeiro_dia, ultimo_dia = calendar.monthrange(2023, 4)
# print(list(calendar.day_name))
# print(calendar.day_name[primeiro_dia])
# print(calendar.day_name[calendar.weekday(2023, 4, ultimo_dia)])

print(calendar.monthcalendar(2023, 4))