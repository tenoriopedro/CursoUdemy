# \w -> [a-zA-Z0-9À-ú_]
# \W -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A (re.ASCII)
# \W -> [^a-zA-Z0-9_] -> re.A (re.ASCII)
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t]
# \S -> [^ \r\n\f\n\t]
# \b -> borda
# \B -> não borda


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

# print(re.findall(r'[a-z]+', texto, flags=re.I))
# print(re.findall(r'[a-zA-Z0-9]+', texto))
# print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
# print(re.findall(r'\w+', texto, flags=re.A))
# print(re.findall(r'\W+', texto, flags=re.A))
# print(re.findall(r'\d+', texto, flags=re.A))
# print(re.findall(r'\D+', texto, flags=re.A))
# print(re.findall(r'\s+', texto, flags=re.A))
# print(re.findall(r'\S+', texto, flags=re.A))
# print(re.findall(r'\be\w+', texto, flags=re.A))
# print(re.findall(r'\w+e\b', texto, flags=re.A))
# print(re.findall(r'\b\w{4}\b', texto, flags=re.A))
# print(re.findall(r'\w{4}', texto, flags=re.A))