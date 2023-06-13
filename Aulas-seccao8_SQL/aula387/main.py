import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD -> Create Read   Update Delete
# SQL ->  INSERT SELECT UPDATE DELETE

# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# DELETE mais cuidadoso
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colubas da tabela
sql = (
    f'INSERT INTO {TABLE_NAME}'
    '(name, weight) '
    'VALUES '
    '(:name, :weight)'
)
# cursor.execute(sql, ['João', 4])
# cursor.executemany(
#     sql,
#     (
#         ('João', 4), ('Pedro', 7)
#     )
# )
# cursor.execute(sql, {'nome': 'João', 'peso': 4})
cursor.executemany(sql, (
    {'name': 'João', 'weight': 4},
    {'name': 'Lucio', 'weight': 7},
    {'name': 'Rui', 'weight': 5},
    {'name': 'Pedro', 'weight': 9},
))
connection.commit()


if __name__ == '__main__':

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id=3'
    )
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="QUALQUER", weight=75.13 '
        'WHERE id=2'
    )
    connection.commit()

    cursor.execute(f'SELECT * FROM {TABLE_NAME}')

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)


    cursor.close()
    connection.close()
