# from log import LogFileMixin, LogPrintMixin

# lp = LogPrintMixin()
# lp.log_error('oi')
# lp.log_sucess('Deu certo')
# lf = LogFileMixin()
# lf.log_error('oi')
# lf.log_sucess('Deu certo')

######################################

from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.ligar()
iphone.ligar()