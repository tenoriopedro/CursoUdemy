## Maria pegou um empréstimo de 1.000.000
## para realizar o pagamento em 5 anos
## a data que em que ela pegou o emprestimo foi
## 20/12/2020 e o vencimento de cada parcela
## é no dia 20 de cada mês
## -- Crie a data do emprestimo
## -- Crie a data do final do empréstimo
## -- Mostre todas as datas de vencimento e o valor de cada parcela

# meses em 5 anos = 60 meses
# valor das parcelas = 16.667 R$

from datetime import datetime
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y'
data_inicio = datetime.strptime('20/12/2022', fmt)
data_fim = data_inicio + relativedelta(years=5)
valor_parcelas = 1000000 / 60

i = 0
mes_parcelas = []
while i < 60:
    parcela = data_inicio + relativedelta(months=1)
    mes_parcelas.append(parcela.strftime(fmt))
    data_inicio = parcela
    i += 1

for p in range(len(mes_parcelas)):
    print(f'{p+1}º parcela dia: {mes_parcelas[p]}, R${valor_parcelas:.2f}'.replace('.',','))