# Meta caracteres: ^ $
# (...)

from pprint import pprint
import re

texto = '''
<p>Frase 1 </p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
'''

# cpf = '147.852.963-12'
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# tags = re.findall(r'<([pdiv]{1,3})>(.+?)<\/\1>', texto)
# tags = re.findall(r'<(?P<tag>[pdiv]{1,3})>(.+?)<\/(?P=tag)>', texto)
# pprint(tags)

print(re.sub(r'(<(.+?)>)(.+?)(</\/2>)', r'\1 MAIS \3 \4', texto))

# for tag in tags:
#     um, dois, tres = tag
#     print(tres)