# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'
response = requests.get(url)
bytes_html = response.content

parsed_html = BeautifulSoup(bytes_html,'html.parser', from_encoding='utf8')

top_jobs_heading = parsed_html.select_one('#intro > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > h2:nth-child(1)')
if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    # print(article)
    if article is not None:
        for p in article.select('p'):
            print(p.text)