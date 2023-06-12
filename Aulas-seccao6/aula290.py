## json.dump e json.load com arquivos

import json
import os

NOME_ARQUIVO = 'aula290.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)


movie = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(movie, arquivo, indent=2, ensure_ascii=False)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    movie_json = json.load(arquivo)
    print(movie_json)