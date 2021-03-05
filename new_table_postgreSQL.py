"""
Создание таблицы PostgreSQL
"""

import psycopg2
from psycopg2 import Error

try:
    # Подключаемся к существующей базе.
    connection = psycopg2.connect(user='postgres',
                                  password='fegBCXtf8',
                                  host='localhost',
                                  port='5432',
                                  database='_db')
    print('Удачное подключения к базе.')
    # Создаем курсор для выполнения операцийй с базой данных.
    cursor = connection.cursor()
    # Пишем запрос SQL
    create_table_query = '''CREATE TABLE mobile
                              (ID INT PRIMARY KEY     NOT NULL,
                              MODEL           TEXT    NOT NULL,
                              PRICE         REAL); '''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
