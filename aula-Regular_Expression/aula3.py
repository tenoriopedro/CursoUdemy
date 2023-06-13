# Quantificadores
# Meta caracteres: ^ $ * ? ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {min, max}


import re

texto = '''
João trouxe     flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi im ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de 
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Jooooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'jo+ão', texto, flags=re.I))