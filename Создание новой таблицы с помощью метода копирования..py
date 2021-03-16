"""
Создаем новую таблицу в базе данных,копируя информацию из другой таблицы.
"""

import psycopg2
from psycopg2 import Error

try:
    # Подключение к существующей базе данных.
    connect = psycopg2.connect(
        user='postgres',
        password='fegBCXtf8',
        port='5432',
        host='localhost',
        database='_db'
    )
    print('Мы подключились к базе данных')
    cursor = connect.cursor()
    database_copy = """create table data_info AS
                       select * from data_shop;"""

    # Выполнение команды
    cursor.execute(database_copy)
    connect.commit()
    print('Таблица создана')

except Error as error:
    print('Ошибка подключения к базе данных', error)
finally:
    if connect:
        cursor.close()
        connect.close()
        print('Соединение с базой данных закрыто')
